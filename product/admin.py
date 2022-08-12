from django.contrib import admin
from .models import Product,UserProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(UserProduct)