from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from main.models import Act, Product


#@login_required(login_url='/accounts/login/')
class ActView(ListView):
    model = Act
    #queryset = Act.objects.all()
    template_name = 'task1.html'
    Act.objects.filter()


class ProductView(ListView):
    model = Product
    template_name = 'task2.html'
