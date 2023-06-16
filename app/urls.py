from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Beer Challenge",
        default_version="v1",
        description="Beer Challenge with DDD and TDD",
        contact=openapi.Contact(email="alcarazjoseph.pedro@gmail.com"),
    ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("api.urls")),
    path("", include("festival.urls")),
]
