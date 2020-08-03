from app.domain.service.market_data_connector import MarketDataConnector
from app.infrastructure.connector.mock_market_data_connector import MockMarketDataConnector


def market_data_connector_factory() -> MarketDataConnector:
    return MockMarketDataConnector()
