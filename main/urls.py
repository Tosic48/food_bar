from django.urls import path
from .views import index, AboutView, ContactView, MenuListView, cake_detail, FBLoginView, FBLogoutView, \
    RegisterUserView, RegisterDoneView

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about-us/', AboutView.as_view(), name='about-us'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('cake_detail/<int:pk>', cake_detail, name='cake_detail'),
    path('accounts/login/', FBLoginView.as_view(), name='login'),
    path('accounts/logout/', FBLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),

]
