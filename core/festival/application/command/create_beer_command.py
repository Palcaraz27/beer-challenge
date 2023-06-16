from dataclasses import dataclass

from festival.cqrs.models import Command


@dataclass(frozen=True)
class CreateBeerCommand(Command):
    name: str
    price: float
