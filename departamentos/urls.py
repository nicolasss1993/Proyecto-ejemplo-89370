from django.urls import path
from departamentos.views import *

urlpatterns = [
    path("", home, name="home"),
    path("departamentos/", departamentos_list, name="departamentos_list"),
    path("departamentos/<int:nro_departamento>/", ver_departamento, name="departamento_detail"),
    
]