from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),                # Página principal
    path("admin/", admin.site.urls),            # Admin Django
    path("productos/", include("tienda.urls")), # Todas las URLs de la app
]
