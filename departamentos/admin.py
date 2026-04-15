from django.contrib import admin
from departamentos.models import DepartamentosMedicos


#admin.site.register(DepartamentosMedicos)


@admin.register(DepartamentosMedicos)
class DepartamentosMedicoAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("nombre", "nro_departamento", "email_dpto")
    # Columnas con enlaces clickeables para entrar en el detalle del registro
    list_display_links = ("nombre",)
    # Campos por los que se pueden buscar
    search_fields = ("nro_departamento",)
    # Filtros laterales
    list_filter = ("fecha_de_creacion",)
    # Orden por defecto
    ordering = ("nro_departamento", "nombre")
    # Campos de solo lectura
    readonly_fields = ("fecha_de_creacion",)
