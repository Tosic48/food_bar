from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about-us/', AboutView.as_view(), name='about-us'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('menu/', MenuListView.as_view(), name='menu'),
    # path('menu/<int:pk>', CakeDetailView.as_view(), name='cake_detail'),
    path('cake_detail/<int:pk>', cake_detail, name='cake_detail'),
    path('accounts/login/', FBLoginView.as_view(), name='login'),
    path('accounts/logout/', FBLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),

]
