from django.contrib import admin
from .models import Menu, Product

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'products')
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['name']
        }),
        ('Кыргызский перевод', {
            'fields': ['name_ky']
        }),
        ('Английский перевод', {
            'fields': ['name_en']
        }),
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'calories', 'proteins', 'fats', 'carbohydrates')
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = [
        ('Русский перевод', {
            'fields': ['name', 'description', 'price', 'calories', 'proteins', 'fats', 'carbohydrates']
        })
        , ('Кыргызский перевод', {
            'fields': ['name_ky', 'description_ky', 'price_ky', 'calories_ky', 'proteins_ky', 'fats_ky', 'carbohydrates_ky']
        })
        , ('Английский перевод', {
            'fields': ['name_en', 'description_en', 'price_en', 'calories_en', 'proteins_en', 'fats_en', 'carbohydrates_en']
        })
    ]