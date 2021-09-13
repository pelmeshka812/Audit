from django.forms import ModelForm

from main.models import Act, Process, SubProcess, Measure, ProtectionLevel, Cert


class ActForm(ModelForm):
    class Meta:
        model = Act
        fields = ['name']


class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class SubProcessForm(ModelForm):
    class Meta:
        model = SubProcess
        fields = '__all__'


class MeasureForm(ModelForm):
    class Meta:
        model = Measure
        fields = '__all__'


class ProtectionLevelForm(ModelForm):
    class Meta:
        model = ProtectionLevel
        fields = '__all__'


class CertForm(ModelForm):
    class Meta:
        model = Cert
        fields = '__all__'
