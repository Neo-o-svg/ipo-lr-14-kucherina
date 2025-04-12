from django.contrib import admin
from .models import Product, ProductCategory, Manufacturer, Cart, CartItem


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Manufacturer)
admin.site.register(Cart)
admin.site.register(CartItem)

