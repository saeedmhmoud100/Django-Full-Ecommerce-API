from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Cart


@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


post_save.connect(create_user_cart, sender=get_user_model())
