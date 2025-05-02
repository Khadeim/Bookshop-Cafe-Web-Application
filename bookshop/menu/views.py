from django.shortcuts import render

from django.http import HttpResponse
from .models import MenuItem

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})
