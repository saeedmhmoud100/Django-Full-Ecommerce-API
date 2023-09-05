from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now

from carts.models import Cart
from users.models import UserAddress


class Order(models.Model):
    _id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), related_name='orders', on_delete=models.CASCADE)

    def user_addresses(self, *args, **kwargs):
        print(self)
        return UserAddress.objects.filter(user=self.user)

    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

    cart = models.OneToOneField(Cart, related_name='order', on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    payMethods = (('cash', 'cash'), ('visa', 'visa'))

    payment_method = models.CharField(max_length=30, choices=payMethods)

    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now(), editable=False)

    total_order_price = models.IntegerField(default=0,blank=True,null=True)

    def save(self, *args, **kwargs):
        # Check if the order is being created for the first time (not updated)
        is_new_order = not self._state.adding

        self.total_order_price = self.cart.total_price
        super().save(*args, **kwargs)
        if not self._id:
            print(self.id)
            self._id = self.id
            self.save()

        if is_new_order:
            user = self.user
            if user:
                # Create a new cart and assign it to the user
                new_cart = Cart.objects.create(user=user)
                user.cart = new_cart
                user.save()


    def __str__(self):
        return self.user.username + " (Order " + str(self.id) + ")"
