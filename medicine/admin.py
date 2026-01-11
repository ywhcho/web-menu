from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'ingredient_name', 'efficacy', 'manufacturer', 'created_at')
    list_filter = ('efficacy', 'manufacturer', 'created_at')
    search_fields = ('product_name', 'ingredient_name', 'manufacturer')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

