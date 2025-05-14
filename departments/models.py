from django.conf import settings
from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='departments', blank=True
    )

    def __str__(self):
        return self.name


class Projects(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    department = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Projects_detail', kwargs={'pk': self.pk})
