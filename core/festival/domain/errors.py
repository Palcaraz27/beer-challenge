from app.cqrs.models import DomainError


class BeerError(DomainError):
    pass

class InvalidBeerIdError(BeerError):
    def __str__(self) -> str:
        return "The id is not valid."

class BeerNameLenghtRuleError(BeerError):
    def __init__(self) -> None:
            super().__init__(message=f"The length of the name must be between a min and max value.")

    def __str__(self) -> str:
        return self.message
