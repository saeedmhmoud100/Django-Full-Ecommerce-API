from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import UserAddress, Cart, CartItem

# Register your models here.

admin.site.unregister(get_user_model())


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    # exclude = ('_id', )
    pass


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    exclude = ('_id',)


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    readonly_fields = ('total_price', )
    class AdminCartItems(admin.TabularInline):
        model = CartItem
        fields = ('product','get_price','quantity')
        readonly_fields = ('get_price',)

    inlines = [AdminCartItems]


# admin.site.register(CartItem)
