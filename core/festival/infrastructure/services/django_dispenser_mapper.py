from core.festival.domain.beer import BeerId
from core.festival.domain.dispenser import Dispenser, DispenserId
from festival.models import Dispenser as DispenserModel


class DjangoDispenserMapper:
    def to_domain(self, dispenser_instance: DispenserModel) -> Dispenser:
        dispenser = Dispenser(
            id=DispenserId(dispenser_instance.uuid),
            beer_id=BeerId(dispenser_instance.beer.uuid),
            flow_volume=dispenser_instance.flow_volume,
            is_open=dispenser_instance.is_open,
            openings=dispenser_instance.openings,
            total_open_time=dispenser_instance.total_open_time,
            open_time=dispenser_instance.open_time      
        )

        return dispenser
