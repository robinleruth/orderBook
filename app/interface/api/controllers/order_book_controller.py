from flask_restplus import Resource

from app.interface.api import api
from app.domain.service.order_book_service_factory import order_book_service_factory


ns = api.namespace('OrderBook', description='OrderBook Controller')


@ns.route('/api/v1/OrderBook')
class OrderBookController(Resource):
    @ns.doc('Get', description='Get best prices')
    def get(self):
        service = order_book_service_factory()
        return 'Ok', 200
