from django.contrib import admin
from .models import Product
from .models import Test

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active', 'category']
    list_display_links = ['name','price']
    list_editable = ['category']
    search_fields = ['name']
    list_filter = ['category']
    # fields = ['name', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Test)

