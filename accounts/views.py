from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,
               'total_orders':total_orders, 'delivered':delivered,
               'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer':customer, 'orders':orders,
               'total_orders':total_orders}

    return render(request, 'accounts/customers.html', context)
