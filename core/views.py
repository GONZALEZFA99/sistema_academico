from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from academico.models import (
    Estudiante,
    Curso,
    Matricula,
    Nota,
)


# ==========================================
# PANEL PRINCIPAL DEL SISTEMA ACADEMICO
# ==========================================

class InicioView(LoginRequiredMixin, TemplateView):

    template_name = "academico/inicio.html"
    login_url = "/admin/login/"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto["total_estudiantes"] = Estudiante.objects.count()
        contexto["total_cursos"] = Curso.objects.count()
        contexto["total_matriculas"] = Matricula.objects.count()
        contexto["total_notas"] = Nota.objects.count()

        return contexto
