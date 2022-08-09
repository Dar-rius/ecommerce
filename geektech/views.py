from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, User
from .form import Login_form, User_form
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

User = User()

# Create your views hered
def index_view(request):
    produits = Produit.objects.all()
    return render(request, "page/home.html", {"produits": produits})

def return_view(request):
    return redirect("home")

def contact_view(request):
    return render(request, "page/contact.html", {})

def commande_view(request):
    return render(request, "page/commande.html",{})

def propos_view(request):
    return render(request, "page/propos.html", {})

def detail_view(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, "page/detail.html", {"produit": produit})


def shop_view(request):
    produits = Produit.objects.all()
    return render(request, "page/shop.html", {"produits": produits})


def register_view(request):
	if request.method == "POST":
		form = User_form(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Creation de compte reussie" )
			return redirect("home")
		messages.error(request, "Creation de compte impossible")
	form = User_form()
	return render (request=request, template_name="page/signup.html", context={"form":form})


def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect("home")


def login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Vous etes connecter {email}.")
                return redirect("home")
            else:
                messages.error(request,"Erreur de connexion")
    else: 
        form = Login_form()
    return render(request, "page/login.html", {"form": form})



def informatique_view(request):
    prod_info = Produit.objects.all()
    return render(request, "page/Informatique.html", {"produits": prod_info})


def bureautique_view(request):
    prod_bureau = Produit.objects.all()
    return render(request, "page/bureautique.html", {"produits": prod_bureau})


def phone_view(request):
    prod_phone = Produit.objects.all()
    return render(request, "page/phone.html", {"produits": prod_phone})


def accesoir_view(request):
    prod_accesoir = Produit.objects.all()
    return render(request, "page/accesoir.html", {"produits": prod_accesoir})


def jeux_view(request):
    prod_jeux = Produit.objects.all()
    return render(request, "page/jeux.html", {"produits": prod_jeux})


def multimedia_view(request):
    prod_multi = Produit.objects.all()
    return render(request, "page/multimedia.html", {"produits": prod_multi})