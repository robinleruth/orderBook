from app.domain.model.command import Command


class UpdateCommand(Command):
    order_id: str
    size_to_update: float
