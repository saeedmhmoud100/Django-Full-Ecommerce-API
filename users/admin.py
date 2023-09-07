from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from users.models import UserAddress


# Register your models here.

# admin.site.unregister(get_user_model())


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    list_display = ('id','username', 'email')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    exclude = ('_id',)

# admin.site.register(CartItem)
