from django.contrib import admin

from carts.models import CartItem, Cart, Coupon


# Register your models here.


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    readonly_fields = ('total_price', )
    exclude = ('_id',)
    class AdminCartItems(admin.TabularInline):
        model = CartItem
        fields = ('product','get_price','quantity')
        readonly_fields = ('get_price',)

    inlines = [AdminCartItems]

@admin.register(Coupon)
class ModelNameAdmin(admin.ModelAdmin):
    exclude = ('_id',)
    list_display = ('id','name','expire','discount')
    list_display_links = ('id','name')
