from result import Err, Ok, Result

from app.cqrs.models import CommandHandler
from core.festival.application.command.close_beer_command import CloseDispenserCommand
from core.festival.domain.dispenser import DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError, DispenserNotFoundError


class CloseDispenserCommandHandler(CommandHandler[CloseDispenserCommand]):
    def __init__(self, dispenser_repository: DispenserRepository) -> None:
        self._dispenser_repository = dispenser_repository

    async def handle(self, command: CloseDispenserCommand)-> Result[None, DispenserError]:
        dispenser = await self._dispenser_repository.get_by_id(DispenserId(command.id))

        if dispenser is None:
            return Err(DispenserNotFoundError(dispenser_id=command.id))

        result = dispenser.close_dispenser()

        if isinstance(result, Err):
            return result

        await self._dispenser_repository.update(dispenser)

        return Ok()
