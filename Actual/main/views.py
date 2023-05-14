from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "main/registration.html"

    def get_success_url(self):
        return reverse_lazy('home')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = "main/login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'main/index.html')


def registration(request):
    return render(request, 'main/registration.html')


def faq(request):
    return render(request, 'main/faq.html')


def communication(request):
    return render(request, 'main/communication.html')


def about(request):
    return render(request, 'main/about.html')

def login(request):
    return render(request, 'main/login.html')
