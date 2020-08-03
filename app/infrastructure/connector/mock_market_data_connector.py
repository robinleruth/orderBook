import time
import random

from typing import List

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.command.command import Command
from app.domain.model.command.add_command import AddCommand
from app.domain.model.command.update_command import UpdateCommand
from app.domain.model.command.cancel_command import CancelCommand
from app.domain.model.side import Side


class MockMarketDataConnector(MarketDataConnector):
    def __init__(self):
        self._id = 1
        self.commands = [AddCommand, UpdateCommand, CancelCommand]
        self.mapping_actions = {
            AddCommand: 'a',
            UpdateCommand: 'u',
            CancelCommand: 'c'
        }
        self.tickers = ['AAPL', 'GOOG', 'SPY']

    def get_actions(self) -> List[Command]:
        market_codes = self._generate_data_stream()
        return self._parse(market_codes)

    def _generate_one_string(self) -> str:
        """
        1st example of data stream:
            data 1: 1568390243|abbb11|a|AAPL|B|209.00000|100
            explanation: timestamp|order id|action|ticker|side|price|size
            data 2: 1568390244|abbb11|u|101
            explanation: timestamp|order id|action|size
            data 3: 1568390245|abbb11|c
            explanation: timestamp|order id|action
        """
        command: Command = random.choice(self.commands)
        timestamp = int(time.time())
        order_id = self._id
        self._id += 1
        action = self.mapping_actions[command]
        ticker = random.choice(self.tickers)
        side = random.choice(['B', 'S'])
        price = random.randint(50, 150)
        size = random.randint(1, 10)
        if command is AddCommand:
            s = '|'.join([str(timestamp), str(order_id), action, ticker, side, str(price), str(size)])
        elif command is UpdateCommand:
            s = '|'.join([str(timestamp), str(order_id), action, str(size)])
        else:
            s = '|'.join([str(timestamp), str(order_id), action])
        return s

    def _generate_data_stream(self) -> List[str]:
        pass

    def _parse(self, codes: List[str]) -> List[Command]:
        return []
