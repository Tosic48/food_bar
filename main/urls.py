from django.urls import path
from .views import index, about, contact, menu

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about-us', about, name='about-us'),
    path('contacts', contact, name='contact'),
    path('menu', menu, name='menu'),

]
