from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produit

# Create your views hered
def index_view(request):
    produits = Produit.objects.all()
    return render(request, "page/home.html", {"produits": produits})

def return_view(request):
    return redirect("home")

def contact_view(request):
    return render(request, "page/contact.html", {})


def propos_view(request):
    return render(request, "page/propos.html", {})

def detail_view(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, "page/detail.html", {"produit": produit})


def shop_view(request):
    produits = Produit.objects.all()
    return render(request, "page/shop.html", {"produits": produits})


def login_view(request):
    return render(request, "page/login.html", {})


def signup_view(request):
    return render(request, "page/signup.html", {})