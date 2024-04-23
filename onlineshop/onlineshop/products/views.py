from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from django.contrib import messages
from .forms import FeedbackForm
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self,request):
        user = "tom"
        products_num = 4
        products = Product.objects.all()[:4]
        
        return render(request, "products/home.html",{
            "name":user,
            "products_num":products_num,
            "products": products,
        })
    
    def post(self,request):
        pass


def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if(product == "suit" or product == "dresses" or product == "shirts" or product == "shoes"):
        return HttpResponse(f"Here is the list of {product}!")
    else:
        return HttpResponse("The page doesn't exist!")

class ProductPageView(View):
    def get(self,request,product_brand,product_slug):
        product = Product.objects.get(slug = product_slug)
        form = FeedbackForm()
        reviews = Feedback.objects.filter(product = product)
        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            "reviews": reviews,
        })
    def post(self,request,product_brand,product_slug):
        product = Product.objects.get(slug = product_slug)
        reviews = Feedback.objects.filter(product = product)
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                product = product,
                rating = form.cleaned_data["rating"],
                text = form.cleaned_data["text"]
            )
            feedback.save()
            messages.success(request,"We received your feedback!")

        return render(request, "products/product.html", {
            "product": product,
            "form":form,
            "reviews": reviews,
        })
        