from dataclasses import dataclass
from asgiref.sync import async_to_sync
from typing import Dict

from result import Result

from app.cqrs.models import R, Command, CommandHandler, DomainError, Query, QueryHandler
from app.cqrs.beer import command_handlers as beer_command_handlers, query_handlers as beer_query_handlers
from app.cqrs.dispenser import command_handlers as dispenser_command_handlers


@dataclass
class CommandDispatcher:
    handlers: Dict[Command, CommandHandler]

    def dispatch(self, command: Command) -> Result[R, DomainError]:
        handler = self.handlers.get(command.__class__)
        if not handler:
            raise RuntimeError(f"Not found handler for {command.__class__}")

        return async_to_sync(handler.handle)(command)


@dataclass
class QueryDispatcher:
    handlers: Dict[Query, QueryHandler]

    def dispatch(self, query: Query) -> Result[R, DomainError]:
        handler = self.handlers.get(query.__class__)
        if not handler:
            raise RuntimeError(f"Not found handler for {query.__class__}")

        return async_to_sync(handler.handle)(query)


command_bus = CommandDispatcher(
    handlers={**beer_command_handlers, **dispenser_command_handlers},
)
query_bus = QueryDispatcher(
    handlers={**beer_query_handlers},
)
