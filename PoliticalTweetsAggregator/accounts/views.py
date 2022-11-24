# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import CustomForm
from django.urls import reverse_lazy
from django.views import generic
class sign_up_view(generic.CreateView):
    form_class = CustomForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

