from dataclasses import dataclass


@dataclass
class Price:
    ticker: str
    bid: float
    ask: float

    @property
    def serialize(self):
        return {
            'ticker': self.ticker,
            'bid': self.bid,
            'ask': self.ask
        }
