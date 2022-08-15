import django


from django.urls import path
from . import views

urlpatterns = [
    path("", views.return_view,),
    path("home/", views.index_view, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("<int:produit_panier_id>/commande/",views.commande_view,name="commande"),
    path("propos/", views.propos_view, name="propos"),
    path("shop/", views.shop_view, name="shop"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.Logout, name='logout'),
    path("signup/",  views.register_view, name="signup"),
    path("<int:produit_id>/detail/", views.detail_view, name="detail"),
    path("informatique/", views.informatique_view, name="informatique"),
    path("bureautique/", views.bureautique_view, name="bureautique"),
    path("phone/", views.phone_view, name="telephone"),
    path("accessoir/", views.accesoir_view, name="accessoir"),
    path("jeux/", views.jeux_view, name="jeux"),
    path("multimedia/", views.multimedia_view, name="multimedia"),
]