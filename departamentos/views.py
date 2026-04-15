from django.shortcuts import render, get_object_or_404, redirect
from departamentos.models import DepartamentosMedicos
from departamentos.forms import DepartamentoMedicoForm
from django.http import Http404

def home(request):
    return render(request, "departamentos/index.html")


def departamentos_list(request):
    nombre = request.GET.get("nombre")
    departamentos_query = DepartamentosMedicos.objects.all()  # QuerySet([Cardio, Traumato, ...])
    if nombre is not None:
        departamentos_query = DepartamentosMedicos.objects.filter(
            nombre__icontains=nombre
        )
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

# GET - Pedir informacion
# POST - Crear/Editar Informacion
# PUT - Actualizar informacion
# DELETE - Eliminar informacion
# ...

def crear_departamento(request):
    if request.method == "POST":
        form = DepartamentoMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("departamentos_list")
    else:
        form = DepartamentoMedicoForm()
    
    return render(request, "departamentos/depatarmento_create.html", {"form": form})
