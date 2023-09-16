from django.db.models.signals import post_save
from django.dispatch import receiver
from carts.models import Cart
from orders.models import Order


@receiver(post_save, sender=Order)
def auto_create_new_cart(sender, instance, created, **kwargs):
    print(created)
    user = instance.user
    if created:

        cart = Cart(user=user)
        cart.save()


post_save.connect(auto_create_new_cart, sender=Order)
