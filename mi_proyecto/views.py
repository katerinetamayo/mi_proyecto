from django.shortcuts import render

def home(request):
    urls = [
        {"path": "/admin/", "name": "Administración Django"},
        {"path": "/productos/", "name": "Lista de productos"},
        {"path": "/productos/crear/", "name": "Crear producto"},
        {"path": "/productos/api/", "name": "API DRF productos"},
    ]
    return render(request, "home.html", {"urls": urls})
