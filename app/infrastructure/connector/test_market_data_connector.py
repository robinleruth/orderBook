from typing import List

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.command.command import Command
from app.domain.model.action import Action


class TestMarketDataConnector(MarketDataConnector):
    def get_actions() -> List[Command]:
        lst = []
        lst.append(AddCommand(Action.ADD,
                              Order(timestamp=1, order_id='5',
                                    ticker='AAPL', side=Side.BUY,
                                    price=10, size=1)))
        lst.append(UpdateCommand(Action.UPDATE, '5', 10)
        lst.append(CancelCommand(Action.CANCEL, '5')
        return lst
