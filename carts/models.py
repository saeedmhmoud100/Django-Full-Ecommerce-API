from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

from products.models import Product


# Create your models here.


class Coupon(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)
    expire = models.DateTimeField(default=now)
    discount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    total_price = models.IntegerField(default=0, blank=True, null=True)
    coupon = models.FloatField(default=0, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def get_all_cart(self):
        l = []
        for i in self.cartItems.all():
            l.append({
                'product': i.product,
                'quantity': i.quantity
            })
        return l

    def __str__(self):
        return f"({self.user.username}) Cart"

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        t = 0
        if self.id and self.cartItems.count() > 0:
            for i in self.cartItems.all():
                t += i.get_price()
            self.total_price = t
        super().save(*args, **kwargs)


class CartItem(models.Model):
    _id = models.IntegerField(null=True,blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(validators=[MinValueValidator(1), ], default=1)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)
    def get_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"({self.product.title}) product for user ({self.cart.user.username})"
