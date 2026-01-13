from django.db import models

# Create your models here.

class Editora(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "editoras"
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"