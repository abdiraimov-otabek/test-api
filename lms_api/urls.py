from django.urls import path

from .views import TodoViewSet

urlpatterns = [
    path('todo/', TodoViewSet.as_view(), name='todo-list'),
    path('todo/<int:id>/', TodoViewSet.as_view(), name='todo-detail'),  # Add this line
]
