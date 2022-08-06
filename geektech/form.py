
from .models import User, Produit
from django.forms import ModelForm
from django import forms

class User_form(ModelForm):
    """
    The default 

    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'firstName', 'adresse', 'phone', 'password', 'password_2']

    def clean_email(self):
        '''
        Verifier si l'email est correcte
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email est correcte")
        return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Veillez taper votre mot de passe")
        return cleaned_data

class Produit_form:
    class Meta:
        model = Produit
        fields = ["nom_produit", "marque_produit", "prix_produit", "quantite_produi", "photo_produit", "cat_produit"]