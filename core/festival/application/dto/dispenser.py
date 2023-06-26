from typing import Any, Dict
from core.festival.domain.dispenser import Dispenser


class DispenserProfitDTO:
    _openings: int
    _total_time_used: str
    _profit: float

    def __init__(self, dispenser: Dispenser, price: float) -> None:
        self._openings = dispenser.openings
        self._total_time_used = dispenser.total_open_time.strftime("%H:%M:%S")
        self._profit = dispenser.profit(price)

    def to_json(self) -> Dict[str, Any]:
        return {
            "openings": self._openings,
            "total_time_used": self._total_time_used,
            "profit": self._profit
        }
