from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views hered
def index_view(request):
    return render(request, "page/home.html", {})

def return_view(request):
    return redirect("home")

def contact_view(request):
    return render(request, "page/contact.html", {})

def commande_view(request):
    return render(request, "page/commande.html",{})

def propos_view(request):
    return render(request, "page/propos.html", {})


def shop_view(request):
    return render(request, "page/shop.html", {})


def login_view(request):
    return render(request, "page/login.html", {})


def signup_view(request):
    return render(request, "page/signup.html", {})