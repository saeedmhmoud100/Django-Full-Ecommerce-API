from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

from Utilities.models import generate_image_filename


# Create your models here.


class Category(models.Model):
    _id = models.IntegerField(blank=True,null=True,editable=False)
    name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField(max_length=40,blank=True,editable=False)
    image = models.ImageField(upload_to=generate_image_filename,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        if self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        if self._id != self.id:
            self._id = self.id

    def __str__(self):
        return self.name