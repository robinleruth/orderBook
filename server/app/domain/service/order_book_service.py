import time

from typing import Dict
from typing import List
from typing import Set
from dataclasses import dataclass
from dataclasses import field
from threading import Thread
from functools import reduce

from app.domain.service.market_data_connector import MarketDataConnector
from app.domain.model.order import Order
from app.domain.model.command.command import Command
from app.domain.model.command.add_command import AddCommand
from app.domain.model.command.update_command import UpdateCommand
from app.domain.model.command.cancel_command import CancelCommand
from app.domain.model.price import Price
from app.domain.model.side import Side
from app.infrastructure.connector.market_data_connector_factory import market_data_connector_factory
from app.infrastructure.log import logger
from app.infrastructure.config import app_config
from app.infrastructure.config import TestConfig


@dataclass
class OrderBookService:
    market_data_connector: MarketDataConnector = field(default_factory=market_data_connector_factory)
    orders_by_id: Dict[str, Order] = field(default_factory=dict)
    orders_by_ticker: Dict[str, List[Order]] = field(default_factory=dict)
    tickers: Set[str] = field(default_factory=set)
    prices_by_ticker: Dict[str, Price] = field(default_factory=dict)

    def __post_init__(self):
        logger.info('Init OrderBookService')
        if not app_config is TestConfig:
            logger.info('Launch refresh from exchange every 5 seconds')
            Thread(target=self.refresh_every_5_seconds).start()

    def get_all(self):
        return [i.serialize for i in self.orders_by_id.values()]

    def add_one(self, order: Order):
        logger.info(f'Adding {order}')
        self.orders_by_id[order.order_id] = order
        if order.ticker not in self.orders_by_ticker:
            self.orders_by_ticker[order.ticker] = []
        self.orders_by_ticker[order.ticker].append(order)

    def update_one(self, order_id: str, size_to_update: float):
        logger.info(f'Trying to update {order_id} size to {size_to_update}')
        if order_id not in self.orders_by_id:
            logger.warn(f'{order_id} not in data structure')
            return
        self.orders_by_id[order_id].size = size_to_update
        logger.info(f'Update succeeded')

    def cancel_one(self, order_id):
        logger.info(f'Cancelling order with id {order_id}')
        if order_id in self.orders_by_id:
            order: Order = self.orders_by_id[order_id]
            del self.orders_by_id[order_id]
            self.orders_by_ticker[order.ticker].remove(order)
            logger.info('Cancel succeeded')
            return
        logger.warn('order_id not in data structure')

    def get_best_price(self) -> List[Price]:
        return self.prices_by_ticker.values()

    def cache_best_prices(self):
        logger.info('Caching best prices')
        for ticker in self.orders_by_ticker:
            orders = self.orders_by_ticker[ticker]
            buy_orders = list(filter(lambda x: x.side == Side.BUY, orders))
            sell_orders = list(filter(lambda x: x.side == Side.SELL, orders))
            try:
                ask = max(sell_orders, key=lambda x: x.price).price
            except:
                ask = 0
            try:
                bid = min(buy_orders, key=lambda x: x.price).price
            except:
                bid = 0
            self.prices_by_ticker[ticker] = Price(ticker, bid, ask)

    def refresh_every_5_seconds(self):
        while True:
            self.refresh_from_exchange()
            self.cache_best_prices()
            time.sleep(app_config.SECONDS_BEFORE_REFRESH)

    def refresh_from_exchange(self):
        logger.info('refresh_from_exchange is called')
        actions: List[Command] = self.market_data_connector.get_actions()
        logger.info(f'{actions} received from exchange')
        for action in actions:
            logger.info(f'Command {action}')
            if isinstance(action, AddCommand):
                action: AddCommand = action
                self.add_one(action.order)
            elif isinstance(action, UpdateCommand):
                action: UpdateCommand = action
                self.update_one(action.order_id, action.size_to_update)
            elif isinstance(action, CancelCommand):
                action: CancelCommand = action
                self.cancel_one(action.order_id)
            else:
                logger.warn(f'{action} not implemented')
