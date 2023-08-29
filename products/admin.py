from django.contrib import admin

from .models import Product


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # fields = ['name', 'image','createdAt','updatedAt']
    # list_display = ['id', 'name', 'updatedAt']
    # list_display_links = ['title', 'id']
    exclude = ('_id',)
    readonly_fields = ['id','slug','createdAt','updatedAt']


admin.site.register(Product, ProductAdmin)
