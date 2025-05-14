from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'A', 'Admin'
        VOLUNTEER = 'V', 'Voluntario'
        STUDENT = 'S', 'Estudiante'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile'
    )

    role = models.CharField(max_length=1, choices=Role, default=Role.VOLUNTEER)

    bio = models.TextField(blank=True)

    avatar = models.ImageField(
        blank=True, null=True, upload_to='cache', default='cache/noavatar.png'
    )

    def __str__(self):
        return f'{self.user.username} {self.role}'

    def get_absolute_url(self):
        return reverse('Profile_detail', kwargs={'pk': self.pk})

    def is_admin(self):
        if self.role == Profile.Role.ADMIN:
            return True
        return False
