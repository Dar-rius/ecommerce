import email
from django.contrib.auth.backends import ModelBackend

from .models import User 

class CustomerBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:
            customer = User.objects.get(email=email)
            if password == customer.password: 
                print("user is login")
                return customer.username
        except User.DoesNotExist:
            print("error in login")