from django.urls import path
from . import views

#listes des differentes liens de la plateforme
urlpatterns = [
    #Les urls du cote user
    path("", views.return_view,),
    path("home/", views.index_view, name="home"),
    path("panier/", views.panier_view, name="panier"),
    path("retirepanier/<int:produit_panier_id>", views.retire_panier_view, name="retire"),
    path("contact/", views.contact_view, name="contact"),
    path("commande/<int:produit_panier_id>/",views.commande_view,name="commande"),
    path("propos/", views.propos_view, name="propos"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.Logout, name='logout'),
    path("signup/",  views.signup_view, name="signup"),
    path("detail/<int:produit_id>/", views.detail_view, name="detail"),
    path("informatique/", views.informatique_view, name="informatique"),
    path("bureautique/", views.bureautique_view, name="bureautique"),
    path("phone/", views.phone_view, name="telephone"),
    path("accessoir/", views.accesoir_view, name="accessoir"),
    path("jeux/", views.jeux_view, name="jeux"),
    path("multimedia/", views.multimedia_view, name="multimedia"),
    path("search/", views.search_view, name="search"),

    #Auth pour le changement de mot de passe
    path("password_reset/", views.password_reset_request, name="password_reset"),

    #les urls de l'admin
    path("administrateur/dashboard/", views.dashboard_view, name="dashboard"),
    path("administrateur/commandes/", views.commandeList_view, name="commandes_list"),
    path("administrateur/commandes/detail/<int:id_commande>/", views.detail_commandes_view, name="detail_commande"),
    path("administrateur/ajout_produit/", views.ajoutProduct_view, name="ajout_produit"),
    path("administrateur/update_produit/<int:id_produit>/", views.updateProd_view, name="update_produit"),
    path("administrateur/porduits/", views.listProd_view, name="list_prod"),
    path("administrateur/delete/produit/<int:id_produit>/", views.deleteProd_view, name="deleteProd"),
    path("administrateur/delete/commande/<int:id_commande>/", views.deleteCommande_view, name="deleteCommande"),
]

