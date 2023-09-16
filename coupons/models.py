from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now


# Create your models here.


class Coupon(models.Model):
    _id = models.IntegerField(null=True, blank=True,editable=False)
    name = models.CharField(max_length=50, unique=True)
    expire = models.DateTimeField(default=now)
    discount = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.id != self._id:
            self._id = self.id
            self.save()
