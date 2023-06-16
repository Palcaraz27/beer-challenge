from dataclasses import dataclass

from app.cqrs.models import Command


@dataclass(frozen=True)
class CreateBeerCommand(Command):
    name: str
    price: float
