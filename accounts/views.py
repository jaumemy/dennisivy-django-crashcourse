from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return render(request, 'accounts/products.html')

def customers(request):
    return render(request, 'accounts/customers.html')
