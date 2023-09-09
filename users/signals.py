from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from carts.models import Cart


@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        c = Cart(user=instance)
        c.save()


# Connect the signal
post_save.connect(create_user_cart, sender=get_user_model())

#
# @receiver(post_save, sender=get_user_model())
# def create_auth_token(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#
#
# # Connect the signal
# post_save.connect(create_user_cart, sender=get_user_model())
