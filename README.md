# ✅ To-Do List Django

Este es un proyecto de una aplicación de lista de tareas (To-Do List) desarrollada con Django.

## ✨ Características

- **📝 Crear tareas**: Añade nuevas tareas a tu lista.
- **👀 Ver tareas**: Visualiza todas las tareas en una página principal.
- **📄 Detalle de tarea**: Haz clic en una tarea para ver su descripción y otros detalles.
- **🔄 Actualizar tareas**: Edita la información de una tarea existente.
- **🗑️ Eliminar tareas**: Borra las tareas que ya no necesites.
- **📊 Estados de tarea**: Las tareas pueden tener los siguientes estados: Pendiente, En Progreso, Completada.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django
- **Base de Datos**: Oracle (configurable en `settings.py`)
- **Variables de Entorno**: python-dotenv para gestionar la configuración sensible.
- **Servidor de archivos estáticos**: whitenoise

## ⚙️ Instalación y Configuración

Sigue estos pasos para configurar el entorno de desarrollo local.

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configura las variables de entorno:**
    Crea un archivo `.env` en el directorio raíz del proyecto (al mismo nivel que `manage.py`) y añade las siguientes variables:
    ```
    SECRET_KEY='tu-secret-key-aqui'
    DB_NAME='nombre-de-tu-bd'
    DB_USER='usuario-de-tu-bd'
    DB_PASSWORD='password-de-tu-bd'
    DB_HOST='host-de-tu-bd'
    DB_PORT='puerto-de-tu-bd'
    ```

5.  **Aplica las migraciones:**
    ```bash
    python manage.py migrate
    ```

## 🚀 Uso

1.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

2.  Abre tu navegador y ve a `http://127.0.0.1:8000/` para empezar a usar la aplicación.

## 📂 Estructura del Proyecto

```
Todolist/
├── manage.py
├── requirements.txt
├── nameproject/         # Directorio de configuración de Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── tasks/               # Aplicación de Django para las tareas
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── templates/
    │   └── tasks/
    │       ├── task_list.html
    │       ├── task_detail.html
    │       └── ...
    └── ...
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* para discutir los cambios que te gustaría hacer.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
