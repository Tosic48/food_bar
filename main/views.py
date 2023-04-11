from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.core.paginator import Paginator

from .forms import RegisterUserForm, ReviewForm, send_email, send_email2
from .models import Cakes, Review
from django.shortcuts import render


# page menu with create review
def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'main/review_created.html')
    else:
        form = ReviewForm()

    review = Review.objects.all()
    return render(request, 'main/index.html', {'review': review, 'form': form})


class AboutView(TemplateView):
    template_name = 'main/about-us.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('subject')
        text = request.POST.get('text')

        send_email2(name, email, phone, text)

        return render(request, 'main/message_sent.html')


# page menu with paginator and send email with detail order
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

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('subject')
        date_time = request.POST.get('subject')
        choice = request.POST.get('text')

        send_email(name, email, phone, date_time, choice)

        return render(request, 'main/order_done.html')


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


class ReviewCreatedView(TemplateView):
    template_name = 'main/review_created.html'


class OrderDoneView(TemplateView):
    template_name = 'main/order_done.html'


class MessageSentView(TemplateView):
    template_name = 'main/message_sent.html'


class CakeDetailView(DetailView):
    model = Cakes
    template_name = 'main/cake_detail.html'
    context_object_name = 'cake'

    def post(self, *args, **kwargs):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        phone = self.request.POST.get('subject')
        date_time = self.request.POST.get('subject')
        choice = self.request.POST.get('text')

        send_email(name, email, phone, date_time, choice)

        return render(self.request, 'main/order_done.html')
