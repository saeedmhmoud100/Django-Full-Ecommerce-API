import json

from django.db import models
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
    description = models.TextField(max_length=600, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    # availableColors = models.FloatField(default=0)
    # image = models.ImageField(upload_to=generate_image_filename)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,null=True)
    # ratingsQuantity = models.ForeignKey(Brand,on_delete=models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #
    # def set_available_colors(self, value):
    #     self.string_list = json.dumps(value)
    #
    # def get_available_colors(self):
    #     return json.loads(self.string_list)

    def __str__(self):
        return self.title
