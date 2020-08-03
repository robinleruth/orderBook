from typing import List

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.command.command import Command
from app.domain.model.command.add_command import AddCommand
from app.domain.model.command.update_command import UpdateCommand
from app.domain.model.command.cancel_command import CancelCommand
from app.domain.model.action import Action
from app.domain.model.order import Order
from app.domain.model.side import Side


class TestMarketDataConnector(MarketDataConnector):
    def get_actions(self) -> List[Command]:
        lst = []
        order = Order(timestamp=1, order_id='5', ticker='AAPL', side=Side.BUY, price=10, size=1)
        a = AddCommand(Action.ADD, order)
        lst.append(a)
        lst.append(UpdateCommand(Action.UPDATE, '5', 10))
        lst.append(CancelCommand(Action.CANCEL, '5'))
        return lst
