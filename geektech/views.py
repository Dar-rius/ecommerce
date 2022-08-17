from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, User, Panier,Commande
from .form import Login_form, User_form, Panier_form
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Q

User = User()

# Create your views here

#la view pour la page d'accueille
def index_view(request):
    produit_info = Produit.objects.filter(cat_produit = "Informatique")[:10]
    produit_multi = Produit.objects.filter(cat_produit = "Multimedia")[:10]
    produit_bureau = Produit.objects.filter(cat_produit = "Bureautique")[:10]
    produit_tele = Produit.objects.filter(cat_produit = "Telephone")[:10]
    produit_accessoir = Produit.objects.filter(cat_produit = "Accesoir")[:10]
    produit_console = Produit.objects.filter(cat_produit = "Console et jeux video")[:10]

    return render(request, "page/home.html", {"produits_info": produit_info, 
                                                "produits_multi": produit_multi,
                                                "produits_bureau": produit_bureau,
                                                "produits_tele": produit_tele,
                                                "produits_accessoir": produit_accessoir,
                                                "produits_console": produit_console})

                                            
# la view pour la page du header
#Ce view a ete creer principalement pour la focntionnalite de recherche
def header_view(request):
    produit_seached = ""

    if 'q' in request.GET:
        q = request.GET['q']
        
        multiple_q = Q(Q(nom_produit__icontains=q) | Q(marque_produit__icontains=q))
        produit_seached = Produit.objects.filter(multiple_q)

    return render(request, "components/header.html", {"produit_seached": produit_seached})


#La view du panier pour afficher toutes donnees du panier du User
def panier_view(request):
    produits_panier = Panier.objects.all()

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
def detail_view(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    autre_produit = Produit.objects.filter(cat_produit=produit.cat_produit)

    if request.method == "POST":
        form = Panier_form(request.POST)

        if form.is_valid():
            quantite_form = form.cleaned_data.get("quantite")
            data_panier = Panier(nom_produit=produit.nom_produit, quantite=quantite_form, pTotal=quantite_form*produit.prix_produit, photo_produit=produit.photo_produit)
            data_panier.save()
            return redirect("home")

    form = Panier_form()
    return render(request, "page/detail.html", {"produit": produit,
                                                    "autre_produit": autre_produit,
                                                    "form": form})


# La view de la page commande pour effectuer une commande
def commande_view(request, produit_panier_id):
    produit = get_object_or_404(Panier, pk=produit_panier_id)
    livraison = 0
    prixTotal = produit.pTotal+livraison

    if request.method == "POST":
        commande = Commande(nom_produit=produit.nom_produit, pTotal=produit.pTotal, quantite=produit.quantite,
                            livraison=livraison, total=produit.pTotal+livraison)
        commande.save()
        return redirect("home")

    return render(request,"page/commande.html", {"produit_panier": produit,
                                                    "livraison": livraison,
                                                    "prixTotal": prixTotal})


#La view pour la page de la boutique
def shop_view(request):
    produit_tendance = Produit.objects.filter(tendance=20)
    produit_info = Produit.objects.filter(cat_produit = "Informatique")[:10]
    produit_multi = Produit.objects.filter(cat_produit = "Multimedia")[:10]
    produit_bureau = Produit.objects.filter(cat_produit = "Bureautique")[:10]
    produit_tele = Produit.objects.filter(cat_produit = "Telephone")[:10]
    produit_accessoir = Produit.objects.filter(cat_produit = "Accesoir")[:10]
    produit_console = Produit.objects.filter(cat_produit = "Console et jeux video")[:10]

    return render(request, "page/shop.html", {"produits_info": produit_info, 
                                                "produits_multi": produit_multi,
                                                "produits_bureau": produit_bureau,
                                                "produits_tele": produit_tele,
                                                "produits_accessoir": produit_accessoir,
                                                "produits_console": produit_console,
                                                "produit_pop": produit_tendance})


#La view pour l'inscription du user
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



# La view pour permettre le user de se deconnecter
def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect("home")


#La view permettant au user de se connecter
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
    prod_accesoir = Produit.objects.filter(cat_produit = "Accessoir")
    return render(request, "page/accesoir.html", {"produits": prod_accesoir})


#La view pour afficher les produit de categories "Jeux "
def jeux_view(request):
    prod_jeux = Produit.objects.filter(cat_produit = 'Console et jeux video')
    return render(request, "page/jeux.html", {"produits": prod_jeux})


#La view pour afficher les produit de categories "Multimedia"
def multimedia_view(request):
    prod_multi = Produit.objects.filter(cat_produit = "Multimedia")
    return render(request, "page/multimedia.html", {"produits": prod_multi})