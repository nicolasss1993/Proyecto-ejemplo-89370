from django.shortcuts import render, get_object_or_404
from departamentos.models import DepartamentosMedicos
from django.http import Http404

def home(request):
    return render(request, "departamentos/index.html")


def departamentos_list(request):
    departamentos_query = DepartamentosMedicos.objects.all()  # QuerySet([Cardio, Traumato, ...])
    contexto = {
        "departamentos_list": list(departamentos_query)
    }
    
    return render(request, "departamentos/departamentos_list.html", contexto)


def ver_departamento(request, nro_departamento):

    departamento = DepartamentosMedicos.objects.get(nro_departamento=nro_departamento)
    departamento2 = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)
    contexto = {
        "departamento_q" : departamento
    }
    
    return render(request, "departamentos/departamento_detail.html", contexto)

    