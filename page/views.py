from django.http.response import HttpResponse
from django.shortcuts import render
from .models import About
from listings.models import Listings

def index(request):
    listings = Listings.objects.all()
    contexts = {
        'listings': listings,
    }
    return render(request,'page/index.html', context=contexts)

def about(request):
    abouts = About.objects.all()
    contexts = {
        'abouts': abouts,
    }
    return render(request, 'page/about.html', context=contexts)
