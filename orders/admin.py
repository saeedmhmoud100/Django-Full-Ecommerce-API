from django.contrib import admin
from orders.models import Order


# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('_id', 'total_order_price')
    actions = None


admin.site.register(Order , OrderAdmin)
