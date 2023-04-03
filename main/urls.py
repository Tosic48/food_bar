from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about-us', AboutView.as_view(), name='about-us'),
    path('contacts', ContactView.as_view(), name='contact'),
    path('menu', MenuListView.as_view(), name='menu'),

    path('accounts/login/', FBLoginView.as_view(), name='login'),
    path('accounts/logout/', FBLogoutView.as_view(), name='logout'),

]
