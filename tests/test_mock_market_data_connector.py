import unittest

from app.infrastructure.connector.mock_market_data_connector import MockMarketDataConnector


class TestMockMarketDataConnector(unittest.TestCase):
    def setUp(self):
        self.connector = MockMarketDataConnector()

    def tearDown(self):
        pass

    def test_generate_single_string(self):
        s = self.connector._generate_one_string()
        print(s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
