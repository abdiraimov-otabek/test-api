from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Just an API for Todo List",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="otabekabdiraimovv@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("lms_api.urls")),  # Your app's URLs
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
