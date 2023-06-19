from django.urls import path

from festival.views import BeerView, BeerByIdView

app_name = "festival"

urlpatterns = [
    path("beer/<uuid:id>", BeerByIdView.as_view(), name="beer CRUD"),
    path("beer", BeerView.as_view(), name="beer CRUD"),
]
