# CREACION DE CRUDS
# Lógica de programación
from django.shortcuts import render

# views.py 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# API's
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# PRODUCTOS 
def lista_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    return render(request, "tienda/producto_lista.html", {"productos": productos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()
    return render(request, "tienda/producto_form.html", {"form": form})

def editar_producto(request, idproducto):
    producto = get_object_or_404(Producto, idproducto=idproducto)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect("lista_productos")
    return render(request, "tienda/producto_form.html", {"form": form})

def eliminar_producto(request, idproducto):
    producto = get_object_or_404(Producto, idproducto=idproducto)
    if request.method == "POST":  # Confirmación antes de borrar
        producto.delete()
        return redirect("lista_productos")
    return render(request, "tienda/producto_confirmar_eliminar.html", {"producto": producto})

# APIS

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
