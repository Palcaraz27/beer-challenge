from django.urls import path

from festival.views import BeerView

app_name = "festival"

urlpatterns = [
    path("beer", BeerView.as_view(), name="beer CRUD"),
]
