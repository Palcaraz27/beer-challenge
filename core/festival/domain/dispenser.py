from dataclasses import dataclass
from datetime import datetime, time
from typing import Optional
import uuid

from result import Err, Ok, Result

from .beer import BeerId
from .errors import DispenserError, DispenserFlowVolumeRuleError, DispenserIsCloseRuleError, DispenserIsOpenRuleError, InvalidDispenserIdError


@dataclass(frozen=True)
class DispenserId:
    value: str

    @classmethod
    def from_string(cls, value: str) -> "DispenserId":
        if not isinstance(value, str):
            raise InvalidDispenserIdError

        return cls(value)

    @classmethod
    def random(cls) -> "DispenserId":
        return cls(str(uuid.uuid4()))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DispenserId) and self.value == other.value


class Dispenser:
    _id: DispenserId
    _beer_id: BeerId
    _flow_volume: float
    _is_open: bool
    _openings: int
    _total_open_time: time
    _open_time: Optional[datetime]

    def __init__(
        self,
        id: DispenserId,
        beer_id: BeerId,
        flow_volume: float,
        is_open: Optional[bool] = False,
        openings: Optional[int] = 0,
        total_open_time: Optional[time] = time(0, 0 ,0),
        open_time: Optional[datetime] = None
    ) -> None:
        self._id = id
        self._beer_id = beer_id
        self._flow_volume = flow_volume
        self._is_open = is_open
        self._openings = openings
        self._total_open_time = total_open_time
        self._open_time = open_time

    @property
    def dispenser_id(self) -> DispenserId:
        return self._id

    @property
    def beer_id(self) -> BeerId:
        return self._beer_id

    @property
    def flow_volume(self) -> float:
        return self._flow_volume

    @property
    def is_open(self) -> bool:
        return self._is_open

    @property
    def openings(self) -> int:
        return self._openings

    @property
    def open_time(self) -> time:
        return self._open_time

    @property
    def total_open_time(self) -> time:
        return self._total_open_time

    def open_dispenser(self) -> Result[None, DispenserError]:
        if self._is_open:
            return Err(DispenserIsOpenRuleError())

        self._is_open = True
        self._open_time = datetime.now()
        self._openings += 1

        return Ok()

    def close_dispenser(self) -> Result[None, DispenserError]:
        if not self._is_open:
            return Err(DispenserIsCloseRuleError())

        self._is_open = False
        self._total_open_time = self._calculate_open_time()
        self._open_time = None

        return Ok()

    def _calculate_open_time(self) -> time:
        open_time = datetime.now() - self._open_time
        total_time_processed = datetime.combine(datetime.now(), self._total_open_time)
        open_time_calculated = total_time_processed + open_time
        return open_time_calculated.time()


class DispenserFactory:
    @staticmethod
    def build(beer_id: str, flow_volume: float) -> Result[Dispenser, DispenserError]:
        if flow_volume <= 0:
            return Err(DispenserFlowVolumeRuleError())

        return Ok(
            Dispenser(
                id=DispenserId.random(),
                beer_id=BeerId(beer_id),
                flow_volume=flow_volume,
            )
        )
