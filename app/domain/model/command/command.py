from dataclasses import dataclass

from app.domain.model.action import Action


@dataclass
class Command:
    action: Action
