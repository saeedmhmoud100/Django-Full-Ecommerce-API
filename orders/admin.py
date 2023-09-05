from django.contrib import admin

from carts.models import CartItem
from orders.models import Order


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('_id','total_order_price')
