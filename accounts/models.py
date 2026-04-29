from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"


class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/avatar.png",
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    pais = models.CharField()
    fecha_de_nacimiento = models.DateField(null=True)
    dni = models.CharField(max_length=15, unique=True)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.username}: {self.first_name}, {self.last_name}"
