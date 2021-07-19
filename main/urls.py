from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from main import views
from main.views import ActView, ProductView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('task1/', ActView.as_view(), name='task1'),
    path('task2/', ProductView.as_view(), name='task2'),
    path('add/act', views.add_act, name='add_act'),
]
