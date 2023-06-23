from dataclasses import dataclass

from app.cqrs.models import Command


@dataclass(frozen=True)
class CloseDispenserCommand(Command):
    id: str
