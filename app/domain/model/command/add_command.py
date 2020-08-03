from dataclasses import dataclass

from app.domain.model.command import Command
from app.domain.model.order import Order


@dataclass
class AddCommand(Command):
    order: Order
