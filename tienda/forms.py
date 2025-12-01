# Formularios y campos que se van a crear con base en models.py

from django import forms
from .models import Cliente, Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']