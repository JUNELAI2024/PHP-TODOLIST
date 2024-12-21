from django.db import models

class Task(models.Model):
    taskdesc = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    urgency_rank = models.IntegerField(default=0)
    assigned_to = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.taskdesc