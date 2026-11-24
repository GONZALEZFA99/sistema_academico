
from django.urls import path

from .views import (
    EstudianteListView,
    EstudianteCreateView,
    EstudianteUpdateView,
    EstudianteDeleteView,
)

app_name = "academico"

urlpatterns = [

    # Listado de estudiantes
    path(
        "estudiantes/",
        EstudianteListView.as_view(),
        name="estudiante_lista"
    ),

    # Registrar estudiante
    path(
        "estudiantes/nuevo/",
        EstudianteCreateView.as_view(),
        name="estudiante_crear"
    ),

    # Editar estudiante
    path(
        "estudiantes/<int:pk>/editar/",
        EstudianteUpdateView.as_view(),
        name="estudiante_editar"
    ),

    # Eliminar estudiante
    path(
        "estudiantes/<int:pk>/eliminar/",
        EstudianteDeleteView.as_view(),
        name="estudiante_eliminar"
    ),

]
