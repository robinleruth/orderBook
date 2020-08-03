from abc import ABCMeta
from abc import abstractmethod
from typing import List

from app.domain.model.command.command import Command


class MarketDataConnector(metaclass=ABCMeta):
    @abstractmethod
    def get_actions(self) -> List[Command]:
        pass
