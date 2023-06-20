from app.cqrs.models import DomainError


# region: Beer Errors
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


class BeerPriceRuleError(BeerError):
    def __init__(self) -> None:
            super().__init__(message=f"Price must be greater than 0.")

    def __str__(self) -> str:
        return self.message


class BeerNotFoundError(BeerError):
    def __init__(self, beer_id: str) -> None:
        super().__init__(message=f"Beer with id {beer_id} not found.")

# endregion

# region: Dispenser Errors
class DispenserError(DomainError):
    pass


class InvalidDispenserIdError(DispenserError):
    def __str__(self) -> str:
        return "The id is not valid."


class DispenserFlowVolumeRuleError(DispenserError):
    def __init__(self) -> None:
            super().__init__(message=f"Flow volume must be greater than 0.")

    def __str__(self) -> str:
        return self.message


class DispenserIsOpenRuleError(DispenserError):
    def __init__(self) -> None:
            super().__init__(message=f"The dispenser is already open.")

    def __str__(self) -> str:
        return self.message


class DispenserIsCloseRuleError(DispenserError):
    def __init__(self) -> None:
            super().__init__(message=f"The dispenser is already close.")

    def __str__(self) -> str:
        return self.message

# endregion