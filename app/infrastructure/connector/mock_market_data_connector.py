from typing import List

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.command.command import Command


class MockMarketDataConnector(MarketDataConnector):
    def get_actions(self) -> List[Command]:
        pass
