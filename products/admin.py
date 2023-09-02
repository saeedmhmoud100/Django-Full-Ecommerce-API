from django.contrib import admin

from .models import Product, Rating, Image
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    search_fields = ('product__title', 'createdAt', 'updatedAt')


class ProductAdmin(admin.ModelAdmin):
    # fields = ['name', 'image','createdAt','updatedAt']
    # list_display = ['id', 'name', 'updatedAt']
    # list_display_links = ['title', 'id']
    exclude = ('_id','imageCover')
    readonly_fields = ['id','slug','ratingsQuantity','createdAt','updatedAt']

    class ImageInline(admin.TabularInline):
        model = Image

    inlines = [ImageInline]

    # def add_images(self, request, queryset):
    #     print(request)
    #     print(queryset)

    # add_images.short_description = "Add images to selected products"

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Rating)
