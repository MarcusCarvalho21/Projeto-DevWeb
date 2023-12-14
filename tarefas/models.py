from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Tarefas(models.Model):
    STATUS=(
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=150)
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True, null=False, blank=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    termino = models.DateField(null=False, blank=False)
    finalizado_em = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo