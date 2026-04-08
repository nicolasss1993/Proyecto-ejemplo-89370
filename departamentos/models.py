from django.db import models


class DepartamentosMedicos(models.Model): # nombre de la tabla
    # Estos van a ser las columnas que guarden la info:
    nombre = models.CharField(max_length=50)
    nro_departamento = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)
    email_dpto = models.EmailField()
    
    def __str__(self):
        return f"Departamento: {self.nombre} / Nro: {self.nro_departamento}"
