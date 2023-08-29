import json

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import JSONField
from django.utils.text import slugify
from django.utils.timezone import now

from Utilities.models import generate_image_filename
from brands.models import Brand
from categories.models import Category


# Create your models here.

class Product(models.Model):
    _id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, blank=True)
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(max_length=600, blank=True)
    quantity = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0.0)])
    sold = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0.0)])
    price = models.FloatField(default=0,validators=[MinValueValidator(0.0)])
    availableColors = models.CharField(max_length=200, blank=True, null=True)
    imageCover = models.ImageField(upload_to=generate_image_filename, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def set_availableColors(self, value):
        self.availableColors = json.dumps(value)

    def get_availableColors(self):
        return json.loads(self.availableColors)
    def ratingsQuantity(self):
        print(self.ratings.first())
        return self.ratings.count()
    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        if not self.slug:
            self.slug = slugify(self.title)

        # self.imageCover = self.images.first().img
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Image(models.Model):
    img = models.ImageField(upload_to=generate_image_filename,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)
    def __str__(self):
        return str(self.product)


class Rating(models.Model):
    _id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='ratings',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0)])
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)