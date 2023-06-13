class DomainError(Exception):
    """Base domain Error"""

    def __init__(self, message: str) -> None:
        self._message: str = message

    def __str__(self) -> str:
        return self._message

    @property
    def message(self) -> str:
        return self._message
