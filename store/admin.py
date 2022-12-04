from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']
    filter = ['price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']
    search_fields = ['first_name', 'phone']
    filter = ['phone']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer',
                    'quantity', 'price', 'address', 'status']
    search_fields = ['product', 'customer']
    filter = ['address']


# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)


# username = Tanushree, email = tanushree7252@gmail.com, password = 1234
