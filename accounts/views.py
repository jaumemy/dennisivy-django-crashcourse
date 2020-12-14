from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.forms import inlineformset_factory

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

def create_order(request, pk):
    order_form_set = inlineformset_factory(Customer, Order,
        fields=("product","status"), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = order_form_set(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method =='POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}

    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        # print('Printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)

def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {"item":order}

    return render(request, 'accounts/delete_order.html', context)
