from django.contrib import admin
from deliveries.models import Customer, Products, Orders

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Orders)

# Register your models here.
