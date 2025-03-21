from django.contrib.auth.models import User
from django.db import models

class SetoresCad(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    usuarios = models.ManyToManyField(User, related_name="setores")
    
    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

    def __str__(self):
        return self.nome
