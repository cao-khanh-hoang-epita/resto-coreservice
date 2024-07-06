from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ApiLog

@receiver(post_save, sender=ApiLog)
def log_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New API log: {instance}")
