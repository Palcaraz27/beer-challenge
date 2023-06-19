from typing import List, Optional

from core.festival.domain.beer import Beer, BeerId
from core.festival.domain.beer_repository import BeerRepository
from core.festival.infrastructure.services.django_beer_mapper import DjangoBeerMapper
from festival.models import Beer as BeerModel


class DjangoBeerRepository(BeerRepository):
    def __init__(self) -> None:
        self.mapper = DjangoBeerMapper()

    async def save(self, beer: Beer) -> None:
        original_instance = await self._get_by_uuid(beer.beer_id.value)

        if original_instance is None:
            return await self._create_beer(beer)

        return original_instance

    async def get_by_id(self, beer_id: BeerId) -> Optional[Beer]:
        instance = await self._get_by_uuid(beer_uuid=beer_id.value)
        return self.mapper.to_domain(instance) if instance else None

    async def get_all(self) -> List[Beer]:
        return [self.mapper.to_domain(beer) async for beer in BeerModel.objects.all()]

    async def _get_by_uuid(self, beer_uuid: str) -> Optional[BeerModel]:
        try:
            instance = await BeerModel.objects.aget(uuid=beer_uuid)
            return instance
        except BeerModel.DoesNotExist:
            return None

    async def _create_beer(self, beer: Beer) -> None:
        await BeerModel.objects.acreate(
            uuid=beer.beer_id.value,
            name=beer.name.value,
            price=beer.price
        )
