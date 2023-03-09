from django.urls import path
from .views import index, about, contact, blog, book_table, elements, gallery, menu, single_blog

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about-us', about, name='about-us'),
    path('contacts', contact, name='contact'),
    path('book_table', book_table, name='book-table'),
    path('blog', blog, name='blog'),
    path('elements', elements, name='elements'),
    path('gallery', gallery, name='gallery'),
    path('menu', menu, name='menu'),
    path('single_blog', single_blog, name='single-blog'),

]
