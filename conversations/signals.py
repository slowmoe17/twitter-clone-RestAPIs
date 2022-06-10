from django.db.models.signals import post_save
from .models import message, conversation
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=message)
def create_conversation(sender, instance, created, **kwargs):
    if created:
        conversation.objects.create(user_one=instance.sender, user_two=instance.receiver)
    else:
        conversation.objects.filter(user_one=instance.sender, user_two=instance.receiver).update(
            user_one=instance.sender, user_two=instance.receiver)
