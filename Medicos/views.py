from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from Medicos.models import Medico



class MedicoListView(ListView):
    model = Medico
    template_name = "medicos/medicos_list.html"
    context_object_name = "medicos_list"

    def get_queryset(self):
        query_list = super().get_queryset()
        query = self.request.GET.get("q")
        
        if query:
            query_list = query_list.filter(nombre__icontains=query)
        return query_list

class MedicoDetailView(DetailView):
    model = Medico
    template_name = "Medicos/medico_detail.html"
    context_object_name = "medico"
    slug_field = "code"
    slug_url_kwarg = "code"


class MedicoCreateView(CreateView):
    model = Medico
    fields = ["nombre", "apellido", "especialidad"]
    # form_class = MedicoForm
    template_name = "Medicos/medico_create.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )

class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ("nombre", "apellido")
    slug_field = "code"
    slug_url_kwarg = "code"

    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )

class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "Medicos/medico_confirm_delete.html"
    success_url = reverse_lazy("medico_list")
    slug_field = "code"
    slug_url_kwarg = "code"