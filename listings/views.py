from django.shortcuts import render, get_object_or_404
from .models import Listings
from rest_framework.decorators import api_view

def index(request):
    listings = Listings.objects.all()
    # count = listings.counts
    contexts = {
        'listings': listings,
    }
    return render(request,'listings/index.html', context=contexts)


def index_items(request):
    listings = Listings.objects.all()
    # count = listings.counts
    contexts = {
        'listings': listings,
    }
    return render(request,'listings/index_items.html', context=contexts)


def detail(request, listing_id='1'):
    listing = get_object_or_404(Listings, id=int(listing_id))
    context = {
        'listing': listing,
    }
    return render(request, 'listings/detail.html', context=context)


@api_view(['GET',])
def search(request):
    listings = Listings.objects.all()
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        listings = listings.filter(bedroom=bedroom)
    if 'bathroom' in request.GET:
        bathroom = request.GET['bathroom']
        listings = listings.filter(bathroom=bathroom)
    if 'minPrice' in request.GET:
        minPrice = request.GET['minPrice']
        listings = listings.filter(price__gte = minPrice)
    if 'maxPrice' in request.GET:
        maxPrice = request.GET['maxPrice']
        listings = listings.filter(price__lte = maxPrice)
    if 'types' in request.GET:
        types = request.GET['types'] 
        listings = listings.filter(types=types)
    if 'condition' in request.GET:
        condition = request.GET['condition']
        listings = listings.filter(condition=condition)
    if 'city' in request.GET:
        city = request.GET['city']
        listings = listings.filter(city=city)
    context = {
        'listings': listings,
    }
    return render(request, 'listings/index.html', context=context)


