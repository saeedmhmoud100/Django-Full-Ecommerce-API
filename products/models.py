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

class Product(models.Model):
    _id = models.IntegerField(blank=True, null=True,editable=False)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, blank=True,editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, editable=False)
    description = models.TextField(max_length=600, blank=True)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0.0)])
    sold = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0.0)])
    price = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    # availableColors = models.CharField(max_length=200, blank=True, null=True)
    imageCover = models.ImageField(upload_to=generate_image_filename, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    users_wishlist = models.ManyToManyField(get_user_model(), related_name='wishList', blank=True,editable=False)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=now, editable=False)

    def all_colors(self):
        l = []
        for i in self.colors.all():
            l.append(i.name)
        return l

    def add_colors(self,colors):
        for color_name in colors:
            color_instance, created = Color.objects.get_or_create(name=color_name, product=self)

    def ratings_quantity(self):
        # print(self.ratings.first())
        return self.ratings.count()

    def add_images(self, images):
        for i in images:
            self.images.add(i)
            self.save()
        return self.images

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        if self.id != self._id:
            self._id = self.id

    def __str__(self):
        return self.title


class Color(models.Model):
    name = models.CharField(max_length=20,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors',blank=True,null=True)
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
        if not self._id:
            self._id = self.id

        # self.imageCover = self.images.first().img
        super().save(*args, **kwargs)
# from django.contrib.auth.models import User
# from products.models import Product
# u = User.objects.all().first()
# p = Product.objects.last()
#
# p = Product.objects.create(title='d',owner=u,quantity=1)
