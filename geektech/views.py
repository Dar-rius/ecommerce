import email
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, User, Panier,Commande
from .forms import Login_form, User_form, Panier_form, Produit_form
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


#Les views pour les parties dont les users peuvent voir

#la view pour la page d'accueille
def index_view(request):
    produit_tendance = Produit.objects.all()
    produit_info = Produit.objects.filter(cat_produit = "Informatique")[:12]
    produit_multi = Produit.objects.filter(cat_produit = "Multimedia")[:12]
    produit_bureau = Produit.objects.filter(cat_produit = "Bureautique")[:12]
    produit_tele = Produit.objects.filter(cat_produit = "Telephone")[:12]
    produit_accessoir = Produit.objects.filter(cat_produit = "Accesoir")[:12]
    produit_console = Produit.objects.filter(cat_produit = "Console et jeux video")[:12]

    return render(request, "page/home.html", {"produits_info": produit_info, 
                                                "produits_multi": produit_multi,
                                                "produits_bureau": produit_bureau,
                                                "produits_tele": produit_tele,
                                                "produits_accessoir": produit_accessoir,
                                                "produits_console": produit_console,
                                                "produit_tendance": produit_tendance})

                                            
#La paage ou se retrouve les produits dont le user recherche
def search_view(request): 
    produit_seached = ""

    if 'q' in request.GET:
        q = request.GET['q']
        
        multiple_q = Q(Q(nom_produit__icontains=q) | Q(marque_produit__icontains=q))
        produit_seached = Produit.objects.filter(multiple_q)

    return render(request, "page/search.html", {"produits": produit_seached})


#La view du panier pour afficher toutes donnees du panier du User
@login_required
def panier_view(request):
    user = request.user
    produits_panier = Panier.objects.filter(client=user)

    return render(request, "page/panier.html", {"produits_panier": produits_panier})


#view permettant de retirer un produit du panier
def retire_panier_view(request, produit_panier_id):
    produit = get_object_or_404(Panier, pk=produit_panier_id)
    produit.delete()
    return redirect("panier")


#la view pour redirection le user vers la page d'accueille
def return_view(request):
    return redirect("home")
    

#La view pour la contact
def contact_view(request):
    return render(request, "page/contact.html", {})


#la view pour la page " a propos "
def propos_view(request):
    return render(request, "page/propos.html", {})


# La view pour la page du detail du produit
@login_required
def detail_view(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    autre_produit = Produit.objects.filter(cat_produit=produit.cat_produit)

    if request.method == "POST":
        form = Panier_form(request.POST)

        if form.is_valid():
            quantite_form = form.cleaned_data.get("quantite")
            form_user = request.user
            data_panier = Panier(client= form_user, nom_produit=produit.nom_produit, quantite=quantite_form, pTotal=quantite_form*produit.prix_produit, photo_produit=produit.photo_produit)
            data_panier.save()
            return redirect("home")

    form = Panier_form()
    return render(request, "page/detail.html", {"produit": produit,
                                                    "autre_produit": autre_produit,
                                                    "form": form,})


# La view de la page commande pour effectuer une commande
@login_required
def commande_view(request, produit_panier_id):
    produit = get_object_or_404(Panier, pk=produit_panier_id)
    produit_selec = Produit.objects.get(nom_produit=produit.nom_produit)
    livraison = 0
    prixTotal = produit.pTotal+livraison

    if request.method == "POST":
        form_user = request.user
        commande = Commande(client= form_user, nom_produit=produit.nom_produit, pTotal=produit.pTotal, quantite=produit.quantite,
                            livraison=livraison, total=produit.pTotal+livraison)
        produit_selec.quantite_produit -= commande.quantite
        produit_selec.tendance+= 5
        produit_selec.save()
        commande.save()
        return redirect("home")

    return render(request,"page/commande.html", {"produit_panier": produit,
                                                    "livraison": livraison,
                                                    "prixTotal": prixTotal})
                                                    

#La view pour l'inscription du user
def signup_view(request):
    if request.method == "POST":
        form = User_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = User_form()
    return render(request, "page/register.html", {"form": form})


# La view pour permettre le user de se deconnecter
def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect("login")


#La view permettant au user de se connecter
def login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                print("le user existe")
                login(request, user)
                return redirect("home")
            else:
                print("le user existe pas")
        else:
            print("le form est pas valide")
    form = Login_form()
    return render(request, "page/login.html", {"form": form})



#La view pour afficher les produit de categories "Informatique"
def informatique_view(request):
    prod_info = Produit.objects.filter(cat_produit = "Informatique")
    return render(request, "page/Informatique.html", {"produits": prod_info})


#La view pour afficher les produit de categories "Bureautique"
def bureautique_view(request):
    prod_bureau = Produit.objects.filter(cat_produit = "Bureautique")
    return render(request, "page/bureautique.html", {"produits": prod_bureau})


#La view pour afficher les produit de categories "Telephone"
def phone_view(request):
    prod_phone = Produit.objects.filter(cat_produit = "Telephone")
    return render(request, "page/phone.html", {"produits": prod_phone})


#La view pour afficher les produit de categories "Accesoir"
def accesoir_view(request):
    prod_accesoir = Produit.objects.filter(cat_produit = "Accesoir")
    return render(request, "page/accesoir.html", {"produits": prod_accesoir})


#La view pour afficher les produit de categories "Jeux "
def jeux_view(request):
    prod_jeux = Produit.objects.filter(cat_produit = 'Console et jeux video')
    return render(request, "page/jeux.html", {"produits": prod_jeux})


#La view pour afficher les produit de categories "Multimedia"
def multimedia_view(request):
    prod_multi = Produit.objects.filter(cat_produit = "Multimedia")
    return render(request, "page/multimedia.html", {"produits": prod_multi})



#Les views pour les parties dont l'admin peut voir

#La view pour le dashboard
def dashboard_view(request):
    commande_count = Commande.objects.all().count()
    produit_count = Produit.objects.all().count()
    return render(request, "admin_page/dashboard.html", {"commande_count": commande_count, 
                                                        "count_prod": produit_count})


#view pour voir tous les produits
def listProd_view(request):
    produits = Produit.objects.all()
    return render(request, "admin_page/produits.html", {"produits": produits})


#La view pour les commandes sur les differentes commandes
def commandeList_view(request):
    commandeList = Commande.objects.all()
    return render(request, "admin_page/commandes.html", {"command_list": commandeList})


#view sur les details de la commandes
def detail_commandes_view(request, id_commande) :
    commande = get_object_or_404(Commande, pk=id_commande)
    image_produit = Produit.objects.get(nom_produit = commande.nom_produit)
    client= User.objects.get(email = commande.client)
    return render(request, "admin_page/detail_commande.html", {"commande":commande,
                                                                "image_produit": image_produit,
                                                                "client": client})


#La view pour ajouter un produit dans la plateforme
def ajoutProduct_view(request):
    if request.method == "POST":
        form = Produit_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = Produit_form()

    return render(request, "admin_page/ajout.html", {"form": form})


#view pour mettre a jour un produit
def updateProd_view(request, id_produit):
 
    produit = get_object_or_404(Produit, pk= id_produit)
    form = Produit_form(request.POST or None, instance = produit)
    if form.is_valid():
        form.save()
        return redirect("list_prod")

    return render(request, "admin_page/updateProd.html", {"form": form, "produit": produit})


#view pour delete un produit
def deleteProd_view(request, id_produit):
    produit = get_object_or_404(Produit, pk=id_produit)
    produit.delete()
    return redirect("list_prod")
