from dataclasses import dataclass

from app.domain.model.command.command import Command


@dataclass
class CancelCommand(Command):
    order_id: str
