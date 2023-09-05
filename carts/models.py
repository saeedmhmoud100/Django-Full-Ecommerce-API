from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

from products.models import Product


class Coupon(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)
    expire = models.DateTimeField(default=now)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')
    total_price = models.FloatField(default=0, blank=True, null=True)
    coupon = models.IntegerField(default=0, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def apply_coupon(self, val):
        try:
            c = Coupon.objects.filter(name=val).first()
            if c.expire > now:
                self.coupon = c.discount
            else:
                self.coupon = 0
        except Coupon.DoesNotExist:
            self.coupon = 0
            return 'Dose Not Exist'

    def get_all_cart_items(self):
        l = []
        for i in self.cartItems.all():
            l.append({
                'product': i.product,
                'quantity': i.quantity
            })
        return l

    def __str__(self):
        return f"({self.user.username}) Cart"

    def calc_total_price(self):
        t = 0.0
        for i in self.cartItems.all():
            t += i.get_all_price()

        if self.coupon > 0.0:
            t *= (1-self.coupon / 100)
        self.total_price = t
        return t

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        super().save(*args, **kwargs)
        if self.cartItems.exists():
            self.calc_total_price()


class CartItem(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(validators=[MinValueValidator(1), ], default=1)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def get_all_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"({self.product.title}) product for user ({self.cart.user.username})"
