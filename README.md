# Aplicación 1: Inicializador y verificador de proyectos Django

**Proyecto:** `init_verificador_django`  
**App:** `verificador`

---

## 1) Crear carpeta del proyecto y entrar

```bash
mkdir init_verificador_django
cd init_verificador_django
````

---

## 2) Crear y activar entorno virtual (venv)

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3) Actualizar pip e instalar Django (con pip)

```bash
python -m pip install --upgrade pip
pip install django
```

---

## 4) Verificar instalación de Django

```bash
django-admin --version
python -m django --version
```

---

## 5) Crear proyecto Django (sin punto, con doble carpeta)

```bash
django-admin startproject init_verificador_django
```

---

## 6) Entrar a la carpeta del proyecto (donde está manage.py)

```bash
cd init_verificador_django
```

---

## 7) Revisar comandos disponibles de manage.py

```bash
python manage.py help
```

---

## 8) Levantar el servidor con manage.py

```bash
python manage.py runserver
```

Detener servidor:

```bash
# CTRL + C
```

---

## 9) Crear la aplicación

```bash
python manage.py startapp verificador
```

---

## 10) Ejecutar migraciones base

```bash
python manage.py migrate
```

---

## 11) Modificar `init_verificador_django/settings.py` (solo lo que agregas)

Agregar la app instalada:

```python
INSTALLED_APPS += [
    "verificador",
]
```

---

## 12) Modificar `init_verificador_django/urls.py` (solo lo que agregas)

Agregar include de la app:

```python
from django.urls import include, path

urlpatterns += [
    path("", include("verificador.urls")),
]
```

---

## 13) Crear `verificador/urls.py`

```python
from django.urls import path

from . import views

app_name = "verificador"

urlpatterns = [
    path("hola/", views.hola, name="hola"),
    path("", views.home, name="home"),
]
```

---

## 14) Modificar `verificador/views.py` (archivo completo)

```python
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hola(request: HttpRequest) -> HttpResponse:
    """
    Saludo mínimo sin templates: respuesta directa.
    """
    return HttpResponse("Hola mundo (sin HTML/template). Proyecto OK ✅")


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
```

---

## 15) Crear carpetas de templates

```bash
mkdir templates
mkdir templates\verificador
```

---

## 16) Crear `templates/verificador/home.html`

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Verificador Django</title>
  </head>
  <body>
    <h1>{{ mensaje }}</h1>

    <p><strong>Ruta:</strong> {{ ruta }}</p>
    <p><strong>Método HTTP:</strong> {{ metodo }}</p>

    <p>Servidor levantado usando <code>python manage.py runserver</code>.</p>
  </body>
</html>
```

---

## 17) Levantar el servidor y probar

```bash
python manage.py runserver
```

Rutas:

* `http://127.0.0.1:8000/hola/` → saludo directo (sin template)
* `http://127.0.0.1:8000/` → home con template
* `http://127.0.0.1:8000/admin/` → admin (si creas superusuario)

---

## 18) Crear superusuario (admin)

```bash
python manage.py createsuperuser
```

---

## 19) Salir del entorno virtual

```bash
deactivate
```
