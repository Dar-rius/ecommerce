from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views hered
def index_view(request):
    return HttpResponse("Je teste")