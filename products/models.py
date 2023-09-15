import json

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import JSONField
from django.utils.text import slugify
from django.utils.timezone import now

from Utilities.models import generate_image_filename
from brands.models import Brand
from categories.models import Category


# Create your models here.


class ProductManager(models.Manager):
    def is_active(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    _id = models.IntegerField(blank=True, null=True, editable=False)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, blank=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=600, blank=True)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0.0)])
    sold = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0.0)])
    price = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    # availableColors = models.CharField(max_length=200, blank=True, null=True)
    imageCover = models.ImageField(upload_to=generate_image_filename)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    users_wishlist = models.ManyToManyField(get_user_model(), related_name='wishlist', blank=True,)
    active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    objects = ProductManager()

    def all_colors(self):
        l = [i.name for i in self.colors.all()]
        return l

    def delete_colors(self):
        self.colors.all().delete()

    def delete_images(self):
        self.images.all().delete()

    def add_colors(self, colors):
        for color_name in colors:
            color_instance, created = Color.objects.get_or_create(name=color_name, product=self)

    def ratings_quantity(self):
        # print(self.ratings.first())
        return self.ratings.count()

    def add_images(self, images):
        for i in images:
            color_instance, created = Image.objects.get_or_create(img=i, product=self)
        # return self.images

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.id != self._id:
            self._id = self.id
            self.save()

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=20, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return str('(' + self.product.title + ') ' + self.name)


class Image(models.Model):
    img = models.ImageField(upload_to=generate_image_filename, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def __str__(self):
        return str(self.product)


# from django.contrib.auth.models import User
# from products.models import Product
# u = User.objects.all().first()
# p = Product.objects.last()
#
# p = Product.objects.create(title='d',owner=u,quantity=1)
