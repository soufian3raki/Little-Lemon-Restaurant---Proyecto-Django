from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu.html', {'menu_items': menu_items})

def menu_item(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    return render(request, 'menu_item.html', {'menu_item': menu_item})

def book(request):
    return render(request, 'book.html')
