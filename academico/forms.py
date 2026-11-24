
from django import forms
from .models import Estudiante


class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante

        fields = [
            "cedula",
            "nombres",
            "apellidos",
            "email",
            "telefono",
            "fecha_nacimiento",
            "carrera",
            "foto",
        ]

        widgets = {
            "cedula": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "nombres": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "apellidos": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),
            "telefono": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "fecha_nacimiento": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                },
                format="%Y-%m-%d"
            ),
            "carrera": forms.Select(
                attrs={"class": "form-select"}
            ),
            "foto": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }
