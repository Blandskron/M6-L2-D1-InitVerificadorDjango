# Aplicación 1: Inicializador y verificador de proyectos Django

Proyecto: **init_verificador_django**  
App: **verificador**

Este documento explica cada parte del proyecto y qué función cumple, usando exactamente lo que fue implementado.

---

## 1) Estructura del proyecto

Al crear el proyecto con:

- `django-admin startproject init_verificador_django`

se genera una **doble carpeta** con el mismo nombre, quedando así:

```

init_verificador_django/
├─ venv/
└─ init_verificador_django/
├─ manage.py
├─ init_verificador_django/
│  ├─ **init**.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ verificador/
│  ├─ views.py
│  ├─ urls.py
│  └─ ...
└─ templates/
└─ verificador/
└─ home.html

````

- La carpeta externa es contenedora (incluye `venv` y el proyecto).
- La carpeta interna contiene el proyecto Django y `manage.py`.
- La carpeta `init_verificador_django/` interna (segunda) es el “paquete” del proyecto (configuración).
- La app `verificador/` es un módulo funcional independiente.

---

## 2) Entorno virtual (`venv`)

Se crea con:

```bash
python -m venv venv
````

Se activa con:

```bash
venv\Scripts\activate
```

Qué significa `venv` aquí:

* El proyecto instala Django **dentro del entorno virtual**, no globalmente.
* `pip install django` instala paquetes en `venv/Lib/site-packages`.
* El comando `python` apunta al intérprete dentro de `venv`.

Por qué importa en este proyecto:

* El objetivo es que la instalación y ejecución dependan solo del proyecto actual.
* Evita dependencias globales y conflictos entre proyectos.

---

## 3) Instalación y verificación de Django

Instalación (dentro del venv):

```bash
pip install django
```

Verificación con herramientas administrativas:

```bash
django-admin --version
python -m django --version
```

Qué verifican:

* `django-admin --version`: comprueba que el ejecutable de Django está disponible.
* `python -m django --version`: comprueba que el módulo Django se puede importar con ese `python`.

---

## 4) `django-admin` vs `manage.py`

### `django-admin`

Es el utilitario global de Django para tareas generales, por ejemplo:

* crear un proyecto (`startproject`)

Se usa antes de tener `manage.py`.

---

### `manage.py`

Es el utilitario administrativo del **proyecto creado**.

* Está ligado a `settings.py` del proyecto
* Sabe cuál configuración usar
* Ejecuta comandos sobre ese proyecto exacto

Ejemplos usados en el proyecto:

* `python manage.py help`
* `python manage.py runserver`
* `python manage.py startapp verificador`
* `python manage.py migrate`
* `python manage.py createsuperuser`

Diferencia clave práctica:

* `django-admin` se usa para iniciar y administrar a nivel general.
* `manage.py` se usa para administrar el proyecto ya creado y su entorno configurado.

---

## 5) `manage.py` (qué representa)

`manage.py` es el “punto de entrada” para comandos del proyecto.

Características:

* Ejecuta comandos con acceso directo a la configuración del proyecto
* Conecta automáticamente con `settings.py` sin que el usuario importe nada manualmente

En este proyecto se usa para:

* levantar el servidor
* crear apps
* aplicar migraciones
* administrar usuario admin

---

## 6) Archivos de configuración del proyecto

Estos archivos viven en:

```
init_verificador_django/init_verificador_django/
```

### `__init__.py`

Marca esa carpeta como paquete Python.
Permite que Django importe módulos como:

* `init_verificador_django.settings`

---

### `settings.py`

Configuración global del proyecto.

En este proyecto, la modificación realizada fue:

* registrar la app `verificador` en `INSTALLED_APPS`

Esto habilita que Django:

* cargue componentes de la app
* encuentre templates (si se configura)
* reconozca migraciones (si existieran)

---

### `urls.py` (del proyecto)

Controla el enrutamiento principal del proyecto.

En este proyecto:

* se delega el enrutamiento a la app `verificador` con `include("verificador.urls")`

Esto crea una arquitectura de enrutamiento en capas:

* proyecto (router principal)
* app (router del módulo)

---

### `wsgi.py` / `asgi.py`

Son puntos de entrada para servidores en despliegue.

* `wsgi.py`: servidores WSGI tradicionales
* `asgi.py`: servidores ASGI (async)

En este proyecto existen para completar el esqueleto estándar generado por Django.

---

## 7) La app `verificador`

Se crea con:

```bash
python manage.py startapp verificador
```

Responsabilidad:

* contener vistas y rutas mínimas para validar que el proyecto funciona.

Archivos usados:

* `verificador/views.py`
* `verificador/urls.py`

---

## 8) Enrutamiento (routing) en la app

### `verificador/urls.py`

Define rutas internas de la app:

* `/hola/` → `views.hola`
* `/` → `views.home`

Aquí se usa `app_name` para namespacing:

```python
app_name = "verificador"
```

Esto permite referenciar rutas por nombre (si se usan templates con `{% url %}`).

---

## 9) Vistas (`verificador/views.py`)

Las vistas reciben un `HttpRequest` y retornan un `HttpResponse`.

En este proyecto hay 2 vistas:

---

### `hola`

```python
return HttpResponse("Hola mundo (sin HTML/template). Proyecto OK ✅")
```

Propósito:

* validar el proyecto con una respuesta directa
* sin templates
* sin HTML externo
* sin dependencias adicionales

Ruta:

* `http://127.0.0.1:8000/hola/`

---

### `home`

```python
return render(request, "verificador/home.html", contexto)
```

Propósito:

* validar el flujo: URL → View → Template
* renderizar un template y pasar contexto

Ruta:

* `http://127.0.0.1:8000/`

---

## 10) Templates

Carpeta creada manualmente:

```
templates/verificador/home.html
```

`home.html` recibe variables del contexto:

* `mensaje`
* `ruta`
* `metodo`

Estas variables se imprimen con `{{ ... }}`.

Este template existe solo como verificación de renderización.

---

## 11) Migraciones base (por qué existen aquí)

Se ejecutó:

```bash
python manage.py migrate
```

Qué hace:

* crea tablas base del framework en SQLite
* permite usar admin/auth/sessions sin configuración extra

Aunque esta app no crea modelos propios, `migrate` valida que:

* el proyecto está funcional a nivel de base de datos
* el proyecto quedó correctamente inicializado

---

## 12) `createsuperuser` y admin

Se ejecuta:

```bash
python manage.py createsuperuser
```

Qué habilita:

* acceso al panel administrativo en:

`http://127.0.0.1:8000/admin/`

Esto valida que:

* `INSTALLED_APPS` base funcionan
* las migraciones base se aplicaron
* el sitio administrativo está operativo

---

## 13) Servidor de desarrollo

Se levanta con:

```bash
python manage.py runserver
```

Qué significa:

* servidor de desarrollo integrado
* ejecuta el proyecto usando los settings del proyecto

Rutas verificadas:

* `/hola/` (HttpResponse directo)
* `/` (Template render)
* `/admin/` (administración)

---

## 14) Qué verifica este proyecto (alcance exacto)

* Crear y activar entorno virtual
* Instalar Django con `pip`
* Verificar instalación (2 métodos)
* Crear proyecto con `django-admin startproject`
* Usar `manage.py` para:

  * `help`
  * `runserver`
  * `startapp`
  * `migrate`
  * `createsuperuser`
* Configurar routing (`urls.py`)
* Confirmar que views y templates funcionan

No incluye:

* modelos
* formularios
* lógica de negocio
* persistencia propia
