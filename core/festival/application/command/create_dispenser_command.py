from dataclasses import dataclass

from app.cqrs.models import Command


@dataclass
class CreateDispenserCommand(Command):
    beer_id: str
    flow_volume: float
