from django import forms
from departamentos.models import DepartamentosMedicos


class DepartamentoMedicoForm(forms.ModelForm):
    class Meta:
        model = DepartamentosMedicos
        fields = ("nombre", "nro_departamento", "email_dpto", "nro_empleados")
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "nro_departamento": forms.NumberInput(attrs={'class': 'form-control'}),
            "email_dpto": forms.EmailInput(attrs={'class': 'form-control'}),
            "nro_empleados": forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DepartamentoMedicoUpdateForm(forms.ModelForm):
    class Meta:
        model = DepartamentosMedicos
        fields = ("nombre", "email_dpto")
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "email_dpto": forms.EmailInput(attrs={'class': 'form-control'}),
        }



class DepartamentoMedicoForm2(forms.Form):
    pass