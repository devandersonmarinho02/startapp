from django.db import models

# Create your models here.

class Agendamento(models.Model):
    hora = models.DateTimeField(auto_now=False, null=True, blank=True)