from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser  # Change this line
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_customer_for_user(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)  # and this line
