from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from urllib import request
from .forms import CustomerRegistrationForm
from .models import products
from django.db.models import Count 
from django.contrib import messages


def home(request):
    return render(request, "app/home.html")

def About(request):
    return render(request, "app/about.html")

def Contact(request):
    return render(request, "app/contact.html")

def Promotion(request):
    return render(request, "app/promotion.html")


class CategoryView(View):
    def get(self,request,val):
        Product =products.objects.filter(category=val)
        title = products.objects.filter(category=val).values('title').annotate(total = Count('title'))
        return render(request,"app/category.html",locals())

class ProductDetails(View):
    def get(self, request, pk):
        product = products.objects.get(pk=pk)  
        return render(request, "app/productdetails.html", locals())
    
class CustomRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())
    
    def post(self,request):
         form = CustomerRegistrationForm( request.POST)
         if form.is_valid():
             form.save() 
             messages.success(request,"congralulations!Registerd Sucessfully! ")
         else:
            messages.warning(request,"Invalid data!!")
         return render(request, 'app/customerregistration.html',locals())