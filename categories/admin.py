from django.contrib import admin

from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image']
    list_display = ['id', 'name', 'updatedAt']

admin.site.register(Category, CategoryAdmin)
