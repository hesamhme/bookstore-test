from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUserModel


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUserModel
    form_class = CustomUserCreationForm


