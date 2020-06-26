from django.db import models

# Create your models here.
class Documento(models.Model):
    nome = models.CharField(max_length=100)
    num = models.CharField(max_length=20)

    def __str__(self):
        return self.nome