from django.urls import path
from .views import add_task, task_list  # Ensure task_list is imported

urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
]