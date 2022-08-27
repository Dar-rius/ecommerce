from pydoc import cli
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.utils.translation import gettext as _

#Moedel du user manager
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


#Model du user
class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

    objects = UserManager()


#categories de produits
CATEGORIES = (
    ('Informatique', 'Informatique'),
    ('Bureautique', 'Bureautique'),
    ('Telephone', 'Telephone'),
    ('Accesoir', 'Accesoir'),
    ('Console et jeux video', 'Console et jeux video'),
    ('Multimedia', 'Multimedia')
)


#Model de produits
class Produit(models.Model):
    nom_produit = models.CharField(max_length=200)
    marque_produit = models.CharField(max_length=100)
    descrip_produit = models.TextField()
    prix_produit = models.IntegerField(default=0)
    quantite_produit = models.IntegerField(default=0)
    cat_produit = models.CharField(max_length=50, choices=CATEGORIES, verbose_name="categories")
    photo_produit = models.ImageField(upload_to='images/')
    tendance = models.IntegerField(default=0)


#Model du panier d'achat
class Panier(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_produit= models.CharField(max_length=200)
    quantite= models.IntegerField(default=0)
    pTotal = models.IntegerField(default=0)
    photo_produit = models.ImageField(upload_to='images_card/')



#Model des commandes
class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=200)
    pTotal = models.IntegerField(default=0)
    quantite = models.IntegerField(default=0)
    livraison = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
