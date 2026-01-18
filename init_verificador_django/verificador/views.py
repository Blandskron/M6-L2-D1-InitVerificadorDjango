from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hola(request: HttpRequest) -> HttpResponse:
    """
    Saludo mínimo sin templates: respuesta directa.
    """
    return HttpResponse("Hola mundo (sin HTML/template). Proyecto OK")

def home(request: HttpRequest) -> HttpResponse:
    """
    Vista mínima para verificar que el proyecto fue creado
    y levantado correctamente usando herramientas administrativas.
    """
    return render(
        request,
        "verificador/home.html",
        {
            "mensaje": "Proyecto Django creado y verificado correctamente",
            "ruta": request.path,
            "metodo": request.method,
        },
    )
