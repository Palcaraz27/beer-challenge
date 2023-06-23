from dataclasses import dataclass

from app.cqrs.models import Command


@dataclass(frozen=True)
class OpenDispenserCommand(Command):
    id: str
