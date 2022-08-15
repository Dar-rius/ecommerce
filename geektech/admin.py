from django.contrib import admin
from .models import User, Produit, Panier
# Register your models here.
admin.site.register(User)
admin.site.register(Produit)
admin.site.register(Panier)