from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from products.models import Product


# Create your models here.


class UserAddress(models.Model):
    _id = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=100)
    details = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postalCode = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='addresses')

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        super().save(*args, **kwargs)

    def __str__(self):
        return str('(' + self.user.username + ') ' + self.alias)

