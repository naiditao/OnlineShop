from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    user = "tom"
    products_num = 4
    return render(request, "products/home.html",{
        "name":user,
        "products_num":products_num,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(request,product):
    if(product == "suit" or product == "dresses" or product == "shirts" or product == "shoes"):
        return HttpResponse(f"Here is the list of {product}!")
    else:
        return HttpResponse("The page doesn't exist!")