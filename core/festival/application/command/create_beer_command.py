from dataclasses import dataclass

from core.utils.models import Command


@dataclass(frozen=True)
class CreateBeerCommand(Command):
    name: str
    price: float
