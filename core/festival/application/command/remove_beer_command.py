from dataclasses import dataclass

from app.cqrs.models import Command


@dataclass(frozen=True)
class RemoveBeerCommand(Command):
    id: str
