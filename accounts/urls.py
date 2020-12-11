from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/', views.customers, name="customers"),
]
