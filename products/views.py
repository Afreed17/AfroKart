from django.shortcuts import render
from . models import Products 
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request,'index.html')

def product_list(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    product_list = Products.objects.all()
    paginator = Paginator(product_list,3)
    product_list = paginator.get_page(page)
    print(product_list)
    return render(request,'products.html',{'products':product_list})

def product_detail(request):
    return render(request,'product_detail.html')