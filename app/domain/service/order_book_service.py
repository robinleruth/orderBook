from typing import Dict
from typing import List
from typing import Set
from dataclasses import dataclass
from dataclasses import field

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.order import Order
from app.infrastructure.connector.market_data_connector_factory import market_data_connector_factory


@dataclass
class OrderBookService:
    market_data_connector: MarketDataConnector = field(default_factory=market_data_connector_factory)
    trades_by_id: Dict[str, Order] = field(default_factory=dict)
    trades_by_ticker: Dict[str, List[Order]] = field(default_factory=dict)
    tickers: Set[str] = field(default_factory=set)

    def get_all(self):
        return [i.serialize for i in trades_by_id.values()]

    def add_one(self, order: Order):
        pass

    def update_one(self):
        pass

    def cancel_one(self):
        pass

    def get_best_price(self):
        pass

    def refresh_from_exchange(self):
        pass
