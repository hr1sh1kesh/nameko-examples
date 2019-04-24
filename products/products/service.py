import logging

from nameko.events import event_handler
from nameko.rpc import rpc,RpcProxy
from nameko_grpc.entrypoint import Grpc
from products import dependencies, schemas
from .products_pb2 import GetProduct, Product
from .products_pb2_grpc import productsStub
from .products_pb2 import UpdateInventoryResponse, UpdateInventoryResponseDetails

logger = logging.getLogger(__name__)

grpc = Grpc.implementing(productsStub)

class ProductsService:

    name = 'products'

    storage = dependencies.Storage()

    @grpc
    def get_product(self, request, context):
        logger.info("recieved grpc request to get products **************** %s", request)
        product = self.storage.get(request.id)
        return Product(**product)

    @rpc
    def list(self):
        products = self.storage.list()
        return schemas.Product(many=True).dump(products).data

    @rpc
    def create(self, product):
        product = schemas.Product(strict=True).load(product).data
        self.storage.create(product)

    @grpc
    def update_products_inventory(self, request, context):
        logger.info("recieved grpc request to update products **************** %s", request)
            
        response = UpdateInventoryResponse(
            updateproductinventoryresponse = [
                UpdateInventoryResponseDetails(
                    id = "1",
                    isupdated = True,
                )
            ]
            )
        return response

    @event_handler('orders', 'order_created')
    def handle_order_created(self, payload):
        for product in payload['order']['order_details']:
            self.storage.decrement_stock(
                product['product_id'], product['quantity'])
