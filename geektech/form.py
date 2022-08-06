
from .models import Produit
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

class User_form(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'firstName', 'adresse', 'phone', 'password', 'password_2']

class Login_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class Produit_form:
    class Meta:
        model = Produit
        fields = ["nom_produit", "marque_produit", "prix_produit", "quantite_produi", "photo_produit", "cat_produit"]