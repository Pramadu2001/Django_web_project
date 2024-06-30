from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from urllib import request
from .models import products
from django.db.models import Count 


def home(request):
    return render(request, "app/home.html")
# Create your views here.

class CategoryView(View):
    def get(self,request,val):
        Product =products.objects.filter(category=val)
        title = products.objects.filter(category=val).values('title').annotate(total = Count('title'))
        return render(request,"app/category.html",locals())
    