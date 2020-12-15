from django.shortcuts import render, redirect
from .models import *
from .forms import order_form, create_user_form
from django.forms import inlineformset_factory
from .filters import order_filter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_page(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = create_user_form()
        if request.method == "POST":
            form = create_user_form(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created succesfully for '+user)

                return redirect('accounts:login')


    context = {'form':form}

    return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.info(request, 'Username or Password incorrect')

        context = {}

        return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)

    return redirect('accounts:home')

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

@login_required(login_url="accounts:login")
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    my_filter = order_filter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {'customer':customer, 'orders':orders,
               'total_orders':total_orders,
               'my_filter':my_filter}

    return render(request, 'accounts/customers.html', context)

@login_required(login_url="accounts:login")
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

@login_required(login_url="accounts:login")
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = order_form(instance=order)
    if request.method =='POST':
        # print('Printing POST:', request.POST)
        form = order_form(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/order_form.html', context)

@login_required(login_url="accounts:login")
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {"item":order}

    return render(request, 'accounts/delete_order.html', context)
