import re
from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=14)

    def save(self, *args, **kwargs):
        numeros = re.sub(r'\D', '', self.telefone)

        if len(numeros) == 11:
            self.telefone = f"({numeros[:2]}){numeros[2:7]}-{numeros[7:]}"
        else:
            raise ValueError("Telefone deve conter 11 dígitos")

        super().save(*args, **kwargs)
    # telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "editoras"
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"