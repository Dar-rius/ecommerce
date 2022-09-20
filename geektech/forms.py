from .models import Produit, User, Panier
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms

class User_form(ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    class Meta:
        model = get_user_model()
        fields = ['email', 'name', 'firstName', 'city', 'quartier', 'phone', 'password', 'password_2']

    def clean_email(self):
        '''
        Verifier si l'email est correcte
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email est existe deja")
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

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class Login_form(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


class Produit_form(ModelForm):
    class Meta:
        model = Produit
        fields = ["nom_produit", "marque_produit", "descrip_produit", "prix_produit", "quantite_produit", "cat_produit", "photo_produit"]

class Panier_form(ModelForm):
    class Meta:
        model = Panier
        fields = ["quantite"]