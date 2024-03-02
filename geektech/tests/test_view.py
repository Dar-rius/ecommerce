#ensemble de test pour le view et formulaire (Interaction)
from django.test import TestCase
from django.urls import reverse
from datetime import date
from datetime import datetime
from ..models import *
from django.contrib.auth import get_user_model


User = get_user_model()
class TestViewForm(TestCase):
    
    #Creation du DB et ajout des valeurs pour tous les champs
    @classmethod
    def setUpTestData(cls):
        for i in range(1, 4):
            Produit.objects.create(
                nom_produit="Iphone",
                marque_produit="test",
                descrip_produit="Un super iphone",
                prix_produit=10000,
                quantite_produit=10,
                cat_produit = 'Telephone'
                ).save()
    

    def setUp(self):
        self.admin = User.objects.create_user(email="med@gmail.com",
            password="#32bis32#",
            admin=True)

        self.user1 = User.objects.create_user(email="mohamed@gmail.com",
            password="#22bis22#")

        self.product = Panier.objects.create(
            client = User.objects.get(id=2),
            nom_produit="Iphone",
            quantite=10,
            pTotal= 10000,
            )


    def testCommand(self):
        C=self.client
        produit = Produit.objects.get(id=1)
        C.login(email=self.user1.email, password=self.user1.password)
        response=C.post(reverse('commande', kwargs={
            'produit_panier_id': self.product.pk
            }),
            data={
                "nom_produit": self.product.nom_produit,
                "pTotal": 10000,
                "quantite": self.product.quantite,
                "total": 10
            })
        self.assertTrue(response, 302)



    def testDeleteCommand(self):
        C=self.client
        produit = Produit.objects.get(id=1)
        C.login(email=self.user1.email, password=self.user1.password)
        response=C.delete(reverse("deleteCommande", kwargs={
            'id_commande':self.product.pk
            }))
        self.assertTrue(response, 302)
