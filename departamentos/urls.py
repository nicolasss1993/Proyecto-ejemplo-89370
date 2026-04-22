from django.urls import path
from departamentos.views import *

urlpatterns = [
    path("", home, name="home"),
    path("departamentos/", departamentos_list, name="departamentos_list"),
    path("departamentos/<int:nro_departamento>/", ver_departamento, name="departamento_detail"),
    path("departamento/crear/", crear_departamento, name="departamento_create"),
    path("departamento/actualizar/<int:nro_departamento>/", actualizar_departamento, name="departamento_update"),
    path("departamento/eliminar/<int:nro_departamento>/", eliminar_departamento, name="departamento_delete"),
    path("departamento/consulta-eliminar/<int:nro_departamento>/", consulta_eliminar_dpto, name="consulta_delete"),
]