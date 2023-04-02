from django.shortcuts import render
from .models import Cakes, Review


def index(request):
    review = Review.objects.all()
    return render(request, 'main/index.html', {'review': review})

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def menu(request):
    cakes = Cakes.objects.all()
    return render(request, 'main/menu.html', {'cakes': cakes})


