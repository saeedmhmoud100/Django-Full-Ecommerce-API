from django.contrib import admin

from .models import Product, Rating, Image, Color


# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    exclude = ('_id',)
    readonly_fields = ['id','slug','ratings_quantity','createdAt','updatedAt']

    class ImageInline(admin.TabularInline):
        model = Image

    class ReviewsInline(admin.TabularInline):
        model = Rating
        exclude = ('review',)
        readonly_fields = ('_id',)
        # fields = ('_id','user','rating')

    class ColorsInline(admin.TabularInline):
        model = Color

        # exclude = ('review',)
        # readonly_fields = ('_id',)

    inlines = [ColorsInline,ImageInline, ReviewsInline]

    # def add_images(self, request, queryset):
    #     print(request)
    #     print(queryset)

    # add_images.short_description = "Add images to selected products"



class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    search_fields = ('product__title', 'createdAt', 'updatedAt')


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('_id',)
    list_display = ('user', 'product', 'rating', 'createdAt', 'updatedAt')
    search_fields = ('product__title', 'user__username', 'rating', 'review')



admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Rating,RatingAdmin)


