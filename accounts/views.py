from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUserModel
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUserModel
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('book_list')


