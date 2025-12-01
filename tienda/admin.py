# Panel de administración

from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)