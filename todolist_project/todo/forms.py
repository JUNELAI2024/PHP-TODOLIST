from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskdesc', 'is_completed', 'urgency_rank', 'assigned_to', 'deadline_date', 'remarks']