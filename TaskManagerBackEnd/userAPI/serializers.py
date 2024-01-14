from rest_framework import serializers

from .models import User
from .models import Task
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'name', 'email', 'password']
    #
    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return super().create(validated_data)

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'owner', 'isDone']