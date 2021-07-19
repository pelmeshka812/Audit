from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.forms import ActForm, ProcessForm, SubProcessForm, MeasureForm, ProtectionLevelForm
from main.models import Act, Product, Process, Sentence


# @login_required(login_url='/accounts/login/')
class ActView(ListView):
    model = Act
    # queryset = Act.objects.all()
    template_name = 'task1.html'
    # Act.objects.filter()


class ProductView(ListView):
    model = Sentence
    template_name = 'task2.html'


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
