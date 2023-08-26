# from django.shortcuts import render # ya no se nesecita, ya que se trabajar con react

from rest_framework import viewsets

from .serializer import TaskSerializer
from .models import Task


# Create your views here.

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()