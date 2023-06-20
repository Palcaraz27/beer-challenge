from datetime import datetime, time
from typing import Optional

from core.festival.domain.beer import BeerId
from core.festival.domain.dispenser import Dispenser, DispenserId


class DispenserBuilder:
    _id: str
    _beer_id: str
    _flow_volume: float
    _is_open: bool
    _openings: int
    _total_open_time: time
    _open_time: Optional[datetime]

    def __init__(self) -> None:
        self._id = "193b926f-4d7a-4b79-9b4c-1128e994a85e",
        self._beer_id = "123e4567-e89b-12d3-a456-526655440012",
        self._flow_volume = 1

    def build(self) -> Dispenser:
        return Dispenser(
            id=DispenserId(self._id),
            beer_id=BeerId(self._beer_id),
            flow_volume=self._flow_volume
        )


class DispenserOpenBuilder(DispenserBuilder):
    def build(self) -> Dispenser:
        dispenser = Dispenser(
            id=DispenserId(self._id),
            beer_id=BeerId(self._beer_id),
            flow_volume=self._flow_volume
        )

        dispenser.open_dispenser()
        return dispenser
