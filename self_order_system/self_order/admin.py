from django.contrib import admin
from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')


@admin.register(models.Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(models.ToppingOrder)
class ToppingOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'topping', 'quantity')


class ToppingOrderInline(admin.TabularInline):
    model = models.ToppingOrder


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ToppingOrderInline]
    list_display = ('table_no', '__str__', 'total_price', 'ordered_at')
    readonly_fields = ['total_price']