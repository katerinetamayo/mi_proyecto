from django.urls import path, include
from . import views

# API DRF
from rest_framework import routers
from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    # CRUD normal
    path("productos/", views.lista_productos, name="lista_productos"),
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("productos/editar/<int:idproducto>/", views.editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:idproducto>/", views.eliminar_producto, name="eliminar_producto"),

    # API DRF
    path("api/", include(router.urls)),
]
