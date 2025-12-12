from rest_framework import serializers
from .models import TaskModel, StatusModel, TaskStatusModel, CommentModel
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields_all__ = ['title', 'description', 'due_date', 'priority']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ['status']

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatusModel
        fields = ['task', 'status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['task', 'comment']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

from datetime import date
def validate_due_date(self, value):
    if value and value < date.today():
        raise serializers.ValidationError("Due date cannot be in the past")
    return value



