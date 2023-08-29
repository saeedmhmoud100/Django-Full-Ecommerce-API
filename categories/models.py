from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    _id = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40,blank=True)
    image = models.ImageField(upload_to='./uploads/categories')
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        if not self._id:
            self._id = self.id
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name