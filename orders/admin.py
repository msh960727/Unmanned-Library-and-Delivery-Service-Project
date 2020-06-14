from django.contrib import admin
from .models import Order, OrderBook



class OrderBookInline(admin.TabularInline):
    model = OrderBook
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'library_location', 'created',
                    'updated', 'pass_word']
    list_filter = ['created', 'updated']
    inlines = [OrderBookInline]


admin.site.register(Order, OrderAdmin)
