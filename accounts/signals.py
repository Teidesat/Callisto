from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=get_user_model())
def create_empty_profile(sender, instance, created, raw, **kwargs):
    if created:
        if not raw:
            Profile.objects.create(user=instance)
