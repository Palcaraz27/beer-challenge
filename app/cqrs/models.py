from abc import abstractmethod
from typing import Any, TypeVar
from typing_extensions import Protocol

R = TypeVar("R")
T_contra = TypeVar("T_contra", contravariant=True)


class DomainError(Exception):
    """Base domain Error"""

    def __init__(self, message: str) -> None:
        self._message: str = message

    def __str__(self) -> str:
        return self._message

    @property
    def message(self) -> str:
        return self._message


class Command:
    ...


class CommandHandler(Protocol[T_contra]):
    """Base handler class."""

    @abstractmethod
    async def handle(self, command: T_contra) -> Any:
        """Handle the command."""
        raise NotImplementedError


class QueryHandler(Protocol[T_contra]):
    """Base handler class."""

    @abstractmethod
    async def handle(self, query: T_contra) -> Any:
        """Handle the query."""
        raise NotImplementedError


Query = Command
