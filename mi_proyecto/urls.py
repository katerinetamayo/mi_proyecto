from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal del sitio
    path('', home, name='home'),

    # Rutas de la app tienda
    path('productos/', include('tienda.urls')),
]
