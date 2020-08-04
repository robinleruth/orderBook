from dataclasses import dataclass

from app.domain.model.side import Side


@dataclass
class Order:
    timestamp: int
    order_id: str
    ticker: str
    side: Side
    price: float
    size: float

    @property
    def serialize(self):
        return {
            'timestamp': self.timestamp,
            'order_id': self.order_id,
            'ticker': self.ticker,
            'side': self.side,
            'price': self.price,
            'size': self.size
        }
