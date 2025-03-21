from django.db import models
from django.contrib.auth.models import User

class SetoresCad(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Setor")
    
    usuarios = models.ManyToManyField(User, related_name="setores")

    def __str__(self):
        return self.nome
    class meta:
        verbose_name = "Novo Setor"
        verbose_name_plural = "Novo Setor"
