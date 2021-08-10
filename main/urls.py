from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from main import views
from main.views import ActView, ProductView, ActFormView, ProcessFormView, SubProcessFormView, ProtectionLevelFormView, \
    MeasureFormView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('task1/', ActView.as_view(), name='task1'),
    path('task2/', ProductView.as_view(), name='task2'),
    path('add/act', views.add_act, name='add_act'),
    path('add/act_form', ActFormView.as_view(), name='add_act_form'),
    path('add/process_form', ProcessFormView.as_view(), name='add_process_form'),
    path('add/subprocess_form', SubProcessFormView.as_view(), name='add_subprocess_form'),
    path('add/measure_form', MeasureFormView.as_view(), name='add_measure_form'),
    path('add/protection_level_form', ProtectionLevelFormView.as_view(), name='add_protection_level_form'),
    path('add/success', TemplateView.as_view(template_name='success_add.html')),
]
