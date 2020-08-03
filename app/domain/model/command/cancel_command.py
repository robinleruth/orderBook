from app.domain.model.command import Command


class CancelCommand(Command):
    order_id: str
