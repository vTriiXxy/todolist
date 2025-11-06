from django.urls import path
from . import views

urlpatterns = [
    # Página principal que muestra la lista de tareas
    path('', views.task_list, name='task_list'),
    # Página para ver el detalle de una tarea
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    # Página para editar una tarea
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    # Ruta para eliminar una tarea
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]