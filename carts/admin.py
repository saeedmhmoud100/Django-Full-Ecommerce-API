from django.contrib import admin

from carts.models import CartItem, Cart


# Register your models here.


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    readonly_fields = ('total_price', )
    class AdminCartItems(admin.TabularInline):
        model = CartItem
        fields = ('product','get_price','quantity')
        readonly_fields = ('get_price',)

    inlines = [AdminCartItems]

