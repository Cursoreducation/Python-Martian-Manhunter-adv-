from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.



class AuthenticationModelForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = 'api-token-auth/'





