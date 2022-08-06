import django


from django.urls import path
from . import views

urlpatterns = [
    path("", views.return_view,),
    path("home/", views.index_view, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("propos/", views.propos_view, name="propos"),
    path("shop/", views.shop_view, name="shop"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("<int:produit_id>", views.detail_view, name="detail")
]