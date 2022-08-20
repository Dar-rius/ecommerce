import django


from django.urls import path
from . import views

#listes des differentes liens de la plateforme
urlpatterns = [
    path("", views.return_view,),
    path("home/", views.index_view, name="home"),
    path("panier/", views.panier_view, name="panier"),
    path("retirepanier/<int:produit_panier_id>", views.retire_panier_view, name="retire"),
    path("contact/", views.contact_view, name="contact"),
    path("commande/<int:produit_panier_id>/",views.commande_view,name="commande"),
    path("propos/", views.propos_view, name="propos"),
    path("shop/", views.shop_view, name="shop"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.Logout, name='logout'),
    path("signup/",  views.register_view, name="signup"),
    path("detail/<int:produit_id>/", views.detail_view, name="detail"),
    path("informatique/", views.informatique_view, name="informatique"),
    path("bureautique/", views.bureautique_view, name="bureautique"),
    path("phone/", views.phone_view, name="telephone"),
    path("accessoir/", views.accesoir_view, name="accessoir"),
    path("jeux/", views.jeux_view, name="jeux"),
    path("multimedia/", views.multimedia_view, name="multimedia"),
    path("search/", views.search_view, name="search"),
    path("administrateur/dasbord", views.dashboard_view, name="dashboard"),
    path("administrateur/commandes", views.commandeList_view, name="commandes_list"),
    path("administrateur/ajout_produit", views.ajoutProduct_view, name="ajout_produit"),
]