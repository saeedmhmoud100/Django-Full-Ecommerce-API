# from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from carts.models import Cart
from users.models import MyUser


@receiver(post_save, sender=MyUser)
def create_user_cart(sender, instance, created, **kwargs):
    print("Signal handler called!")
    if created:
        Cart.objects.create(user=instance)


# Connect the signal
post_save.connect(create_user_cart, sender=MyUser)
