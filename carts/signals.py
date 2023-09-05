from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from carts.models import Cart, CartItem


@receiver(post_save, sender=CartItem)
def calc_total_cart_price(sender, instance, created, **kwargs):
    instance.cart.total_price = instance.cart.calc_total_price()
    instance.cart.save()


# Connect the signal
post_save.connect(calc_total_cart_price, sender=CartItem)


@receiver(post_delete, sender=CartItem)
def calc_total_cart_price(sender, instance, **kwargs):
    instance.cart.total_price = instance.cart.calc_total_price()
    instance.cart.save()


# Connect the signal
post_delete.connect(calc_total_cart_price, sender=CartItem)