from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')

def blog(request):
    return render(request, 'main/blog.html')

def book_table(request):
    return render(request, 'main/book-table.html')

def elements(request):
    return render(request, 'main/elements.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def menu(request):
    return render(request, 'main/menu.html')

def single_blog(request):
    return render(request, 'main/single-blog.html')