from django.db import models
# from clients.models import Client
# Create your models here.

class Task(models.Model):
    title: models.CharField(max_length=200)
    description: models.TextField(blank=True)
    done: models.BooleanField(default=False)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE) //Manejar clientes luego