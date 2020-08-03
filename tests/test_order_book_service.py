import unittest

from app.domain.service.order_book_service import OrderBookService
from app.domain.model.side import Side
from app.domain.model.order import Order


class TestOrderBookService(unittest.TestCase):
    def setUp(self):
        self.service = OrderBookService()
        order1 = Order(timestamp=1, order_id='1', ticker='AAPL', side=Side.BUY,
                       price=10, size=1)
        order2 = Order(timestamp=1, order_id='2', ticker='AAPL', side=Side.SELL,
                       price=9, size=1)
        self.service.add_one(order1)
        self.service.add_one(order2)

    def tearDown(self):
        pass

    def test_data_structure(self):
        self.asssertEqual(1, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
