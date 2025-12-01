from django.shortcuts import render

from django.shortcuts import render

def home(request):
    urls = [
        {"path": "/admin/", "name": "Administración Django"},
        {"path": "/productos/", "name": "Lista de productos"},
        {"path": "/productos/crear/", "name": "Crear producto"},
    ]
    return render(request, "home.html", {"urls": urls})
