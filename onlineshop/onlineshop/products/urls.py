from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "home"),
    path('products/<product>',views.product_cat, name = "product_cat"), #suit product category
    path('signup',views.signup, name = "signup"),  #sign up page
    path('products/<product_brand>/<product_slug>',views.product_page, name = "product_page")
]