from django.contrib import admin

from .models import Product, Rating, Image


# Register your models here.


class ProductImageAdmin(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    # fields = ['name', 'image','createdAt','updatedAt']
    # list_display = ['id', 'name', 'updatedAt']
    # list_display_links = ['title', 'id']
    exclude = ('_id','imageCover')
    readonly_fields = ['id','slug','ratingsQuantity','createdAt','updatedAt']

    # inlines  = [ProductImageAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Rating)
