from django.contrib import admin

from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image','createdAt','updatedAt']
    list_display = ['id', 'name', 'updatedAt']
    list_display_links = ['name', 'id']
    readonly_fields = ['createdAt','updatedAt']


admin.site.register(Category, CategoryAdmin)
