from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrManager

class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrManager]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Task.objects.all()
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrManager]

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Task.objects.all()
        return Task.objects.filter(user=user)
