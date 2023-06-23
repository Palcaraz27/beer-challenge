from result import Err, Ok, Result

from app.cqrs.models import CommandHandler
from core.festival.application.command.open_dispenser_command import OpenDispenserCommand
from core.festival.domain.dispenser import DispenserId
from core.festival.domain.dispenser_repository import DispenserRepository
from core.festival.domain.errors import DispenserError, DispenserNotFoundError


class OpenDispenserCommandHandler(CommandHandler[OpenDispenserCommand]):
    def __init__(self, dispenser_repository: DispenserRepository) -> None:
        self._dispenser_repository = dispenser_repository

    async def handle(self, command: OpenDispenserCommand)-> Result[None, DispenserError]:
        dispenser = await self._dispenser_repository.get_by_id(DispenserId(command.id))

        if dispenser is None:
            return Err(DispenserNotFoundError(dispenser_id=command.id))

        result = dispenser.open_dispenser()

        if isinstance(result, Err):
            return result

        await self._dispenser_repository.update(dispenser)

        return Ok()
