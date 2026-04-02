from django.contrib import admin
from api.models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_id", "user", "created_at", "status",)
    inlines = [
        OrderItemInline
    ]

admin.site.register(Order, OrderAdmin)