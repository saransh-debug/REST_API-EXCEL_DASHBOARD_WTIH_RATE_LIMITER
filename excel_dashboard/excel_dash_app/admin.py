from django.contrib import admin
from .models import brand , Seller , product , order , filemodel
# Register your models here.

admin.site.register(brand)
admin.site.register(Seller) 
admin.site.register(product)
admin.site.register(order)
admin.site.register(filemodel)