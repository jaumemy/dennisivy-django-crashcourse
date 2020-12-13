from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/<str:pk>/', views.customers, name="customers"),
]
