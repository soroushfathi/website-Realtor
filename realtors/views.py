from django.shortcuts import render
from .models import Realtor

def realtors_index(request):
    realtors = Realtor.objects.all()
    contexxts = {
        'realtors': realtors, #  for jinjo
    }
    return render(request, 'realtors/realtors_index.html', context=contexxts)

def realtor_detail(request):
    realtors = Realtor.objects.all()
    contexxts = {
        'realtors': realtors, #  for jinjo
    }
    return render(request, 'realtors/realtors_index.html', context=contexxts)

