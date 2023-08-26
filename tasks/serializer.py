from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = '__all__'  # '__all__' is the same way to pass all the fields of the model
        fields = ('id', 'title', 'description', 'done')