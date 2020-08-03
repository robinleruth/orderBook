from dataclasses import dataclass

from app.domain.model.command.command import Command


@dataclass
class UpdateCommand(Command):
    order_id: str
    size_to_update: float
