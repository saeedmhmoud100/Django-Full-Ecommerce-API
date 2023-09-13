from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from carts.models import Cart, CartItem
from orders.models import Order


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

# @receiver(post_save, sender=Order)
# def create_new_cart_when_order(sender, instance, created, **kwargs):
#     if created:
#         # Create a new cart and assign it to the user
#         new_cart = Cart.objects.create(user=instance.user)
#         instance.user.cart = new_cart
#         instance.user.save()
#
#
# post_save.connect(calc_total_cart_price, sender=Order)
