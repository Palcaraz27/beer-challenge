from dataclasses import dataclass
from asgiref.sync import async_to_sync
from typing import Any, Dict, Type

from result import Result

from festival.cqrs.models import R, Command, CommandHandler, DomainError
from festival.cqrs.beer import command_handlers as beer_command_handlers


@dataclass
class CommandDispatcher:
    handlers: Dict[Type[Any], CommandHandler[Any]]

    def dispatch(self, command: Command) -> Result[R, DomainError]:
        handler = self.handlers.get(command.__class__)
        if not handler:
            raise RuntimeError(f"Not found handler for {command.__class__}")

        return async_to_sync(handler.handle)(command)


command_bus = CommandDispatcher(
    handlers={**beer_command_handlers},
)
