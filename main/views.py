from django.shortcuts import render
from .models import Cakes, Review


def index(request):
    review_1 = Review.objects.first()
    review_2 = Review.objects.all()[1]
    return render(request, 'main/index.html', {'review_1': review_1, 'review_2': review_2})

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def menu(request):
    cakes = Cakes.objects.all()
    return render(request, 'main/menu.html', {'cakes': cakes})


