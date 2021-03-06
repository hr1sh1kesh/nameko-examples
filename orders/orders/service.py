from nameko.events import EventDispatcher
from nameko.rpc import rpc,RpcProxy
from nameko_grpc.entrypoint import Grpc
from nameko_sqlalchemy import DatabaseSession
from nameko_grpc.dependency_provider import GrpcProxy
from nameko_grpc.client import Client

from orders.exceptions import NotFound
from orders.models import DeclarativeBase, Order, OrderDetail
from orders.schemas import OrderSchema
from .orders_pb2 import OrderDeletedResponse, OrderDetailResponse, OrderResponse
from .orders_pb2_grpc import ordersStub
from .products_pb2_grpc import productsStub
from .products_pb2 import UpdateInventoryRequest, UpdateInventoryResponse, UpdateInventoryResponseDetails, UpdateProductInventoryRequestDetails, GetProduct
from logging import getLogger
# import grpc

grpc = Grpc.implementing(ordersStub)
log = getLogger(__name__)

class OrdersService:
    name = 'orders'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    products_grpc = GrpcProxy("http://products.examples.svc.cluster.local:50051", productsStub)

    @grpc
    def get_order(self, request, context):
        log.debug("------- Get Order ------- %s", request)
        order = self.db.query(Order).get(request.id)

        if not order:
            raise NotFound('Order with id {} not found'.format(request.id))

        return self._order_response(order)

    @grpc
    def create_order(self, request, context):
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
        log.info("------- Create Order with ------- %s", request.order_details)
        self.db.add(order)
        self.db.commit()

        log.info("--- Created order --- %s", order)
        
        updateInventoryRequest = UpdateInventoryRequest(
            updateproductinventorydetails=[
                UpdateProductInventoryRequestDetails(
                    id = order_details.product_id,
                    quantity = order_details.quantity,
            )
            for order_details in order.order_details
            ]
        )
        
        log.info("------- Update Inventory of Products after Order creation ------- %s", updateInventoryRequest)

        with Client("//products.examples.svc.cluster.local:50051", productsStub) as client:
            response = client.update_products_inventory(updateInventoryRequest)
            print(response)

        # self.event_dispatcher('order_created', {
        #     'order': order.to_dict(),
        # })

        return self._order_response(order)

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