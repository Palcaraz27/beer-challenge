from django.urls import path

from festival.views import BeerView, BeerByIdView, DispenserView

app_name = "festival"

urlpatterns = [
    path("beer/<uuid:id>", BeerByIdView.as_view(), name="beer CRUD"),
    path("beer", BeerView.as_view(), name="beer CRUD"),
    path("dispenser", DispenserView.as_view(), name="dispenser CRUD"),
]
