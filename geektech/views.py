import email
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Produit
from .form import Login_form, User_form
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout


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

class SignupView(FormView):
    """sign up user view"""
    form_class = User_form
    template_name = 'page/signup.html'
    def form_valid(self, form):

        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        if user is not None:
            return redirect("home")

        return super().form_valid(form)


def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect("home")


class LoginView(FormView):
    """login view"""

    form_class = Login_form
    template_name = 'page/login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')