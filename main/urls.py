from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about-us'),
    path('contact', views.contact, name='contact'),

]
