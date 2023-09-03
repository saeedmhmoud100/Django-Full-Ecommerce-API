from django.contrib import admin

from users.models import UserAddress


# Register your models here.

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    exclude = ('_id', )