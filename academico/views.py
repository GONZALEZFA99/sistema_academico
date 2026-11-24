
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from core.mixins import FiltroCamposMixin
from .models import Estudiante, Carrera
from .forms import EstudianteForm
from django.contrib import messages


class EstudianteListView(FiltroCamposMixin, ListView):
    model = Estudiante
    template_name = "academico/estudiante_lista.html"
    context_object_name = "estudiantes"
    paginate_by = 10

    # Título que utilizaremos en el reporte PDF
    titulo_reporte = "Reporte de Estudiantes"

    # Columnas disponibles
    campos_disponibles = {
        "cedula": "Cédula",
        "nombres": "Nombres",
        "apellidos": "Apellidos",
        "carrera__nombre": "Carrera",
    }

    # Columnas que aparecerán inicialmente
    campos_por_defecto = [
        "cedula",
        "nombres",
        "apellidos",
        "carrera__nombre",
    ]

    # Ordenar los estudiantes alfabéticamente
    ordering = ["apellidos", "nombres"]



    def get_queryset(self):
        queryset = super().get_queryset()

        # Buscar por nombre, apellido, cédula o carrera
        busqueda = self.request.GET.get("buscar", "").strip()


        if busqueda:
            condiciones = Q()

            condiciones.add(
                Q(cedula__icontains=busqueda), Q.OR
            )
            condiciones.add(
                Q(nombres__icontains=busqueda), Q.OR
            )
            condiciones.add(
                Q(apellidos__icontains=busqueda), Q.OR
            )
            condiciones.add(
                Q(carrera__nombre__icontains=busqueda), Q.OR
            )

            queryset = queryset.filter(condiciones)


        # Filtrar por la carrera seleccionada
        carrera_id = self.request.GET.get("carrera", "").strip()

        if carrera_id.isdigit():
            queryset = queryset.filter(
                carrera_id=int(carrera_id)
            )

        return queryset

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        # Mostrar las carreras disponibles
        contexto["carreras"] = Carrera.objects.order_by("nombre")

        # Conservar la carrera seleccionada
        contexto["carrera_seleccionada"] = (
            self.request.GET.get("carrera", "")
        )

        # Relacionar cada estudiante con su fila
        contexto["filas_con_estudiante"] = list(
            zip(contexto["object_list"], contexto["filas"])
        )

        return contexto




# ==========================================
# REGISTRAR ESTUDIANTE
# ==========================================

class EstudianteCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "academico/estudiante_form.html"
    success_url = reverse_lazy("academico:estudiante_lista")
    success_message = "Estudiante registrado correctamente."
    login_url = "/admin/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ==========================================
# EDITAR ESTUDIANTE
# ==========================================

class EstudianteUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView
):
    model = Estudiante
    form_class = EstudianteForm
    template_name = "academico/estudiante_form.html"
    success_url = reverse_lazy("academico:estudiante_lista")
    success_message = "Estudiante actualizado correctamente."
    login_url = "/admin/login/"



# ==========================================
# ELIMINAR ESTUDIANTE
# ==========================================

class EstudianteDeleteView(
    LoginRequiredMixin,
    DeleteView
):
    model = Estudiante
    template_name = "academico/estudiante_confirmar_eliminar.html"
    success_url = reverse_lazy("academico:estudiante_lista")
    login_url = "/admin/login/"

    def form_valid(self, form):
        respuesta = super().form_valid(form)

        messages.success(
            self.request,
            "Estudiante eliminado correctamente."
        )
        return respuesta
