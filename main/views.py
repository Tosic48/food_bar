from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.core.paginator import Paginator

from .forms import RegisterUserForm
from .models import Cakes, Review


def index(request):
    review = Review.objects.all()
    return render(request, 'main/index.html', {'review': review})


class AboutView(TemplateView):
    template_name = 'main/about-us.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


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


class FBLoginView(LoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True


class FBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'