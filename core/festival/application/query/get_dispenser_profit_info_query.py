from dataclasses import dataclass

from app.cqrs.models import Query


@dataclass(frozen=True)
class GetDispenserProfitInfoQuery(Query):
    id: str