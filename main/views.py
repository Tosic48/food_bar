from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.core.paginator import Paginator

from .forms import RegisterUserForm, ReviewForm
from .models import Cakes, Review
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    review = Review.objects.all()
    return render(request, 'main/index.html', {'review': review, 'form': form})


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
        paginator = Paginator(context['object_list'], 3)
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


def cake_detail(request, pk):
    cake = Cakes.objects.get(pk=pk)
    context = {
        'cake': cake,

    }
    return render(request, 'main/cake_detail.html', context)
