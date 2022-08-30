from pydoc import cli
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, AbstractBaseUser
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
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
       
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
       
        user = self.create_user(email, password)
        user.staff = True
        user.save(using=self._db)
        return user


#Model du user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    # notice the absence of a "Password field", that is built in.

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.staff


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
    commander = models.BooleanField(default=False)



#Model des commandes
class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=200)
    pTotal = models.IntegerField(default=0)
    quantite = models.IntegerField(default=0)
    livraison = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    photo_produit = models.ImageField(upload_to='images_commande/')

