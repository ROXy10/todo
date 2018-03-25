from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Todo