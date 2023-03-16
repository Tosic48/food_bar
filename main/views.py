from django.shortcuts import render
from .models import Cake

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def menu(request):
    cakes = Cake.objects.all()
    context = {'cakes': cakes}
    return render(request, 'main/menu.html', context=context)
