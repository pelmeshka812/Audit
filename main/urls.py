from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from main import views
from main.views import ActView, ProductView, ActFormView, ProcessFormView, SubProcessFormView, ProtectionLevelFormView, \
    MeasureFormView, ActDetail, ProcessDetail, SubProcessDetail, MeasureDetail, TypeListView, TypeDetail, CertView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('task1/', ActView.as_view(), name='task1'),
    path('task2/', TypeListView.as_view(), name='task2'),
    path('add/act', views.add_act, name='add_act'),
    path('add/act_form', ActFormView.as_view(), name='add_act_form'),
    path('add/process_form', ProcessFormView.as_view(), name='add_process_form'),
    path('add/subprocess_form', SubProcessFormView.as_view(), name='add_subprocess_form'),
    path('add/measure_form', MeasureFormView.as_view(), name='add_measure_form'),
    path('add/protection_level_form', ProtectionLevelFormView.as_view(), name='add_protection_level_form'),
    path('add/cert', CertView.as_view(), name='cert'),
    path('add/success', TemplateView.as_view(template_name='success_add.html')),
    path('process/<int:pk>/', ActDetail.as_view(), name='act_detail'),
    path('subprocess/<int:pk>/', ProcessDetail.as_view(), name='process_detail'),
    path('measure/<int:pk>/', SubProcessDetail.as_view(), name='subprocess_detail'),
    path('sentence/<int:pk>/', MeasureDetail.as_view(), name='measure_detail'),
    path('type/sentence/<int:pk>/', TypeDetail.as_view(), name='type_detail'),
    #url(r'act_detial/(?P<pk>\d+)$', ActDetial.as_view(), name='act_detail')
]
