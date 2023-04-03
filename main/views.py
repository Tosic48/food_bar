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

# def menu(request):
#     cakes = Cakes.objects.all()
#     objects_per_page = 3
#     paginator = Paginator(cakes, objects_per_page)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'main/menu.html', {'page_obj': page_obj})

class MenuListView(ListView):
    template_name = 'main/menu.html'
    context_object_name = 'menu'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        objects_per_page = 3
        paginator = Paginator(context['object_list'], objects_per_page)
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return super().get_context_data(**context)

    def get_queryset(self):
        return Cakes.objects.all()