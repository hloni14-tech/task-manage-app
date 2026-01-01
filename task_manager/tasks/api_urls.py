from django.urls import path
from .api_views import (
    TaskListCreateAPIView,
    TaskRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='api-task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDeleteAPIView.as_view(), name='api-task-detail'),
]
