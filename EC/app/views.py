from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from urllib import request
from .forms import CustomerProfileForm, CustomerRegistrationForm
from .models import Customer, products
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
    
class profileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html", locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully!")
        else:
            messages.warning(request, "Invalid data!!")
        
        # Ensure it always returns an HttpResponse
        return render(request, "app/profile.html", locals())
    
class updateaddress(View):
     def get(self,request,pk):
         add = Customer.objects.get(pk=pk)
         form =CustomerProfileForm(instance=add)
         return render(request,'app/updateAddress.html',locals())
     def post (self,request,pk):
         form =CustomerProfileForm(request.POST)
         if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile saved successfully!")
         else:
            messages.warning(request, "Invalid data!!")
         return redirect("address")
        

def address(request):
    add = Customer.objects.filter(user =request.user)
    return render(request,"app/address.html",locals()) 
