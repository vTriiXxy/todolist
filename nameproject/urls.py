from django.contrib import admin
from django.urls import path, include

# Este es el enrutador principal de tu proyecto.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Le dice a Django que busque las URLs de la app 'tasks' en el archivo tasks/urls.py
    path('', include('tasks.urls')),
]
