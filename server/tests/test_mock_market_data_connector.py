import unittest

from app.infrastructure.connector.mock_market_data_connector import MockMarketDataConnector
from app.domain.model.command.add_command import AddCommand
from app.domain.model.command.update_command import UpdateCommand
from app.domain.model.command.cancel_command import CancelCommand


class TestMockMarketDataConnector(unittest.TestCase):
    def setUp(self):
        self.connector = MockMarketDataConnector()

    def tearDown(self):
        pass

    def test_generate_single_string(self):
        s = self.connector._generate_one_string()
        print(s)

    def test_generate_strings(self):
        lst = self.connector._generate_data_stream()
        print(lst)

    def test_parse_one_is_add_command(self):
        s = '1568390243|abbb11|a|AAPL|B|209.00000|100'
        command = self.connector._parse_one(s)
        self.assertTrue(isinstance(command, AddCommand))

    def test_parse_one_is_update_command(self):
        s = '1568390244|abbb11|u|101'
        command = self.connector._parse_one(s)
        self.assertTrue(isinstance(command, UpdateCommand))

    def test_parse_one_is_cancel_command(self):
        s = '1568390244|abbb11|c'
        command = self.connector._parse_one(s)
        self.assertTrue(isinstance(command, CancelCommand))

    def test_parse(self):
        s = ['1568390243|abbb11|a|AAPL|B|209.00000|100',
             '1568390244|abbb11|u|101', '1568390244|abbb11|c']
        commands = self.connector._parse(s)
        self.assertEqual(3, len(commands))
        print(commands)


if __name__ == '__main__':
    unittest.main(verbosity=2)
