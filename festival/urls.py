from django.urls import path

from festival.views import (
    BeerView,
    BeerByIdView,
    DispenserView,
    DispenserByIdView,
    DispenserOpenView,
    DispenserCloseView,
    DispenserProfitView,
)

app_name = "festival"

urlpatterns = [
    path("beer/<uuid:id>", BeerByIdView.as_view(), name="beer get by id"),
    path("dispenser/close/<uuid:id>", DispenserCloseView.as_view(), name="open dispenser"),
    path("dispenser/profit/<uuid:id>", DispenserProfitView.as_view(), name="open dispenser"),
    path("dispenser/open/<uuid:id>", DispenserOpenView.as_view(), name="open dispenser"),
    path("dispenser/<uuid:id>", DispenserByIdView.as_view(), name="dispenser get by id"),
    path("beer", BeerView.as_view(), name="beer CRUD"),
    path("dispenser", DispenserView.as_view(), name="dispenser CRUD"),
]
