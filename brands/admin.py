from django.contrib import admin

from .models import Brand


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    fields = ['name', 'image','createdAt','updatedAt']
    list_display = ['id', 'name', 'updatedAt']
    list_display_links = ['name', 'id']
    readonly_fields = ['createdAt','updatedAt']

admin.site.register(Brand, BrandAdmin)
