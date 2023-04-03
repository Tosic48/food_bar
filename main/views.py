from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator
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

def menu(request):
    cakes = Cakes.objects.all()
    objects_per_page = 3
    paginator = Paginator(cakes, objects_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/menu.html', {'page_obj': page_obj})

# class MenuView(TemplateView):
#     template_name = 'main/menu.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cakes'] = Cakes.objects.all()
#         return context