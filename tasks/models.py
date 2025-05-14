# Create your models here.
from django.conf import settings
from django.db import models

from departments.models import Department


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    departments = models.ManyToManyField(Department, related_name='tasks', blank=True)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tasks', blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
