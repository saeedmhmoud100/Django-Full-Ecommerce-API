from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.timezone import now

from products.models import Product


# Create your models here.

class Reviews(models.Model):
    _id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return self.product.title + ' (' + str(self.rating) + ')'

    def save(self, *args, **kwargs):

        # self.imageCover = self.images.first().img
        super().save(*args, **kwargs)
        if not self._id:
            self._id = self.id
            self.save()