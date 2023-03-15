from django.shortcuts import render
from main.models import Сakes

def index(request):
    # cakes = Cakes.object.all()
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def menu(request):
    return render(request, 'main/menu.html')
