from django.contrib import admin

from coupons.models import Coupon


# Register your models here.


@admin.register(Coupon)
class ModelNameAdmin(admin.ModelAdmin):
    exclude = ('_id',)
    list_display = ('id','name','expire','discount')
    list_display_links = ('id','name')
