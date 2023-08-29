from django.contrib import admin

from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image']


admin.site.register(Category, CategoryAdmin)
