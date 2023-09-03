from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import UserAddress

# Register your models here.

admin.site.unregister(get_user_model())


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    # exclude = ('_id', )
    pass


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    exclude = ('_id',)


# admin.site.register(CartItem)
