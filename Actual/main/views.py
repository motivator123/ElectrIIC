from django.shortcuts import render

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