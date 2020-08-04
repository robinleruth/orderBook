from functools import lru_cache

from app.domain.service.order_book_service import OrderBookService


@lru_cache
def order_book_service_factory() -> OrderBookService:
    return OrderBookService()
