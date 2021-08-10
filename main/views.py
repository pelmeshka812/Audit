from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, CreateView

from main.forms import ActForm, ProcessForm, SubProcessForm, MeasureForm, ProtectionLevelForm
from main.models import Act, Product, Process, Sentence, SubProcess, Measure, ProtectionLevel


# @login_required(login_url='/accounts/login/')
class ActView(ListView):
    model = Act
    # queryset = Act.objects.all()
    template_name = 'task1.html'
    # Act.objects.filter()


class ProductView(ListView):
    model = Sentence
    template_name = 'task2.html'


class ActFormView(CreateView):
    model = Act
    template_name = 'add_act_form.html'
    fields = ['name']
    success_url = 'process_form'


class ProcessFormView(CreateView):
    model = Process
    template_name = 'add_process_form.html'
    fields = '__all__'
    success_url = 'subprocess_form'


class SubProcessFormView(CreateView):
    model = SubProcess
    template_name = 'add_subprocess_form.html'
    fields = '__all__'
    success_url = 'measure_form'


class MeasureFormView(CreateView):
    model = Measure
    template_name = 'add_measure_form.html'
    fields = '__all__'
    success_url = 'protection_level_form'


class ProtectionLevelFormView(CreateView):  
    model = ProtectionLevel
    template_name = 'add_protection_level_form.html'
    fields = '__all__'
    success_url = 'success'


# class ActFormView(FormView):
#     template_name = 'add_act_form.html'
#     form_class = ActForm
#     success_url = '/add/process_form/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)
#
#
# class ProcessFormView(FormView):
#     template_name = 'add_process_form.html'
#     form_class = ProcessForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)


#
# class Process(DetailView):
#     model = Process
#     template_name = 'task1_process.html'
#
#     Process.objects.filter(act_id=Act.objects.)
# def get_process(request, act):
#     Process.objects.filter(act_id=act)
#     process = get_object_or_404(Process, act_id=act)


def add_act(request):
    if request.method == 'POST':
        form_act = ActForm(request.POST)
        form_process = ProcessForm(request.POST)
        form_subprocess = SubProcessForm(request.POST)
        form_measure = MeasureForm(request.POST)
        form_level = ProtectionLevelForm(request.POST)
        if form_act.is_valid():
            act = form_act.save()
            act.save()
        if form_process.is_valid():
            process = form_process.save()
            process.save()
        if form_subprocess.is_valid():
            subprocess = form_subprocess.save()
            subprocess.save()
        if form_measure.is_valid():
            measure = form_measure.save()
            measure.save()
        if form_level.is_valid():
            level = form_level.save()
            level.save()
    else:
        form_act = ActForm()
        form_process = ProcessForm()
        form_subprocess = SubProcessForm()
        form_measure = MeasureForm()
        form_level = ProtectionLevelForm()

    return render(request, 'add_act.html',
                  {'form_act': form_act, 'form_process': form_process, 'form_subprocess': form_subprocess,
                   'form_measure': form_measure, 'form_level': form_level})
