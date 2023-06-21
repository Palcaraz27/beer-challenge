from result import Err, Ok, Result

from app.cqrs.models import CommandHandler
from core.festival.application.command.create_dispenser_command import CreateDispenserCommand
from core.festival.domain.dispenser import DispenserFactory
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError


class CreateDispenserCommandHandler(CommandHandler[CreateDispenserCommand]):
    def __init__(self, dispenser_repository: DispenserRepository) -> None:
        self._dispenser_repository = dispenser_repository

    async def handle(self, command: CreateDispenserCommand) -> Result[None, DispenserError]:
        dispenser = DispenserFactory.build(beer_id=command.beer_id, flow_volume=command.flow_volume)

        if isinstance(dispenser, Err):
            return dispenser

        await self._dispenser_repository.save(dispenser.ok())

        return Ok()
