from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Cakes, Review


def index(request):
    review = Review.objects.all()
    return render(request, 'main/index.html', {'review': review})

class AboutView(TemplateView):
    template_name = 'main/about-us.html'

class ContactView(TemplateView):
    template_name = 'main/contact.html'

# def menu(request):
#     cakes = Cakes.objects.all()
#     return render(request, 'main/menu.html', {'cakes': cakes})

class MenuView(TemplateView):
    template_name = 'main/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cakes'] = Cakes.objects.all()
        return context