import unittest

from app.domain.service.order_book_service import OrderBookService
from app.domain.model.side import Side
from app.domain.model.order import Order
from app.infrastructure.connector.test_market_data_connector import TestMarketDataConnector


class TestOrderBookService(unittest.TestCase):
    def setUp(self):
        connector = TestMarketDataConnector()
        self.service = OrderBookService(connector)
        order1 = Order(timestamp=1, order_id='1', ticker='AAPL', side=Side.BUY,
                       price=10, size=1)
        order2 = Order(timestamp=1, order_id='2', ticker='AAPL', side=Side.SELL,
                       price=9, size=1)
        self.service.add_one(order1)
        self.service.add_one(order2)

    def tearDown(self):
        pass

    def test_data_structure(self):
        self.assertEqual(2, len(self.service.trades_by_id.values()))
        self.assertEqual(1, len(self.service.trades_by_ticker.keys()))
        self.assertEqual(2, len(self.service.trades_by_ticker['AAPL']))

    def test_update_one(self):
        self.assertEqual(1, self.service.trades_by_id['1'].size)
        self.service.update_one('1', 40)
        self.assertEqual(40, self.service.trades_by_id['1'].size)
        o = list(filter(lambda x: x.order_id == '1', self.service.trades_by_ticker['AAPL']))[0]
        self.assertEqual(40, o.size)

    def test_cancel_one(self):
        self.service.cancel_one('1')
        self.assertTrue('1' not in self.service.trades_by_id)
        self.assertEqual(1, len(self.service.trades_by_ticker['AAPL']))

    def test_get_all(self):
        print(self.service.get_all())

    def test_refresh_from_exchange(self):
        self.service.refresh_from_exchange()


if __name__ == '__main__':
    unittest.main(verbosity=2)
