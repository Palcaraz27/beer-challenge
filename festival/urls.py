from django.urls import path

from festival.views import BeerView, BeerByIdView, DispenserView, DispenserByIdView

app_name = "festival"

urlpatterns = [
    path("beer/<uuid:id>", BeerByIdView.as_view(), name="beer get by id"),
    path("dispenser/<uuid:id>", DispenserByIdView.as_view(), name="dispenser get by id"),
    path("beer", BeerView.as_view(), name="beer CRUD"),
    path("dispenser", DispenserView.as_view(), name="dispenser CRUD"),
]
