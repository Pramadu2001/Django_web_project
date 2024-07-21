from django.contrib import admin
from.models import products,Customer
# Register your models here.
@admin.register(products)
class productModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discount_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','zipcode']

