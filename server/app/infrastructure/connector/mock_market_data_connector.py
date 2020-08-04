import time
import random

from typing import List

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.command.command import Command
from app.domain.model.command.add_command import AddCommand
from app.domain.model.command.update_command import UpdateCommand
from app.domain.model.command.cancel_command import CancelCommand
from app.domain.model.side import Side
from app.domain.model.order import Order
from app.domain.model.action import Action


class MockMarketDataConnector(MarketDataConnector):
    def __init__(self):
        self._id = 1
        self.commands = [AddCommand, UpdateCommand, CancelCommand]
        self.mapping_actions = {
            AddCommand: 'a',
            UpdateCommand: 'u',
            CancelCommand: 'c'
        }
        self.mapping_letter_to_actions = {
            'a': AddCommand,
            'u': UpdateCommand,
            'c': CancelCommand
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
        if side == 'S':
            price = random.randint(101, 150)
        else:
            price = random.randint(50, 99)
        size = random.randint(1, 10)
        if command is AddCommand:
            s = '|'.join([str(timestamp), str(order_id), action, ticker, side, str(price), str(size)])
        elif command is UpdateCommand:
            s = '|'.join([str(timestamp), str(order_id), action, str(size)])
        else:
            s = '|'.join([str(timestamp), str(order_id), action])
        return s

    def _generate_data_stream(self) -> List[str]:
        nb_message = random.randint(1, 10)
        return [self._generate_one_string() for _ in range(nb_message)]

    def _parse(self, codes: List[str]) -> List[Command]:
        return [self._parse_one(code) for code in codes]

    def _parse_one(self, code: str) -> Command:
        lst = code.split('|')
        if len(lst) == 7:
            timestamp = int(lst[0])
            order_id = lst[1]
            # action = self.mapping_letter_to_actions[lst[2]]
            ticker = lst[3]
            side = Side(lst[4])
            price = float(lst[5])
            size = float(lst[6])
            order = Order(timestamp, order_id, ticker, side, price, size)
            return AddCommand(Action.ADD, order)
        elif len(lst) == 4:
            timestamp = int(lst[0])
            order_id = lst[1]
            # action = self.mapping_letter_to_actions[lst[2]]
            size = lst[3]
            return UpdateCommand(Action.UPDATE, order_id, size)
        else:
            timestamp = int(lst[0])
            order_id = lst[1]
            return CancelCommand(Action.CANCEL, order_id)

