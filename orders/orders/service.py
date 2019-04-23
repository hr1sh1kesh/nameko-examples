from nameko.events import EventDispatcher
from nameko.rpc import rpc,RpcProxy
from nameko_sqlalchemy import DatabaseSession
from nameko_grpc.entrypoint import Grpc

from orders.exceptions import NotFound
from orders.models import DeclarativeBase, Order, OrderDetail
from orders.schemas import OrderSchema
from .orders_pb2 import OrderDeletedResponse, OrderDetailResponse, OrderResponse
from .orders_pb2_grpc import ordersStub
from logging import getLogger


grpc = Grpc.implementing(ordersStub)
log = getLogger(__name__)

class OrdersGrpcService:
    name = 'ordersgrpc'
    
    orders_rpc = RpcProxy('orders')

    @grpc
    def get_order(self, request, context):
        log.debug("recieved grpc request to get orders **************** %s", request)
        order = self.orders_rpc.get_order(request.id)
        return self._order_response(order)
        

    @grpc
    def create_order(self, request, context):
        log.info(request)
        order = Order(
            order_details=[
                OrderDetail(
                    product_id=order_detail.product_id,
                    price=order_detail.price,
                    quantity=order_detail.quantity,
                )
                for order_detail in request.order_details
            ]
        )
        log.info("request received, order %s", request.order_details)
        order = self.orders_rpc.create_order(order.order_details)

        return self._order_response(order)

    def _order_response(self, order):
        return OrderResponse(
            id=order.id,
            order_details=[
                OrderDetailResponse(
                    id=order_detail.id,
                    product_id=order_detail.product_id,
                    price=str(order_detail.price),
                    quantity=order_detail.quantity,
                )
                for order_detail in order.order_details
            ],
        )

class OrdersService:
    name = 'orders'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_order(self, order_id):
        order = self.db.query(Order).get(order_id)

        if not order:
            raise NotFound('Order with id {} not found'.format(order_id))

        return OrderSchema().dump(order).data

    @rpc
    def create_order(self, order_details):
        log.info("Order Details %s", order_details)
        order = Order(
            order_details=[
                OrderDetail(
                    product_id=order_detail['product_id'],
                    price=order_detail['price'],
                    quantity=order_detail['quantity']
                )
                for order_detail in order_details
            ]
        )
        self.db.add(order)
        self.db.commit()

        order = OrderSchema().dump(order).data

        self.event_dispatcher('order_created', {
            'order': order,
        })

        return order

    @rpc
    def update_order(self, order):
        order_details = {
            order_details['id']: order_details
            for order_details in order['order_details']
        }

        order = self.db.query(Order).get(order['id'])

        for order_detail in order.order_details:
            order_detail.price = order_details[order_detail.id]['price']
            order_detail.quantity = order_details[order_detail.id]['quantity']

        self.db.commit()
        return OrderSchema().dump(order).data

    @rpc
    def delete_order(self, order_id):
        order = self.db.query(Order).get(order_id)
        self.db.delete(order)
        self.db.commit()

    def _order_response(self, order):
        return OrderResponse(
            id=order.id,
            order_details=[
                OrderDetailResponse(
                    id=order_detail.id,
                    product_id=order_detail.product_id,
                    price=str(order_detail.price),
                    quantity=order_detail.quantity,
                )
                for order_detail in order.order_details
            ],
        )