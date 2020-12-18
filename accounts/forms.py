from django.forms import ModelForm
from .models import Order, Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class order_form(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class create_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class customer_form(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
