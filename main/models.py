from django.db import models


class Act(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class SubProcess(models.Model):
    identifier = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=250)
    measures = models.ManyToManyField('Measure')

    def __str__(self):
        return self.name


class Process(models.Model):
    identifier = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=250)
    subprocesses = models.ManyToManyField(SubProcess, related_name='subprocesses')
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE, null=True, related_name='processes')

    def __str__(self):
        return self.name


class ProtectionLevel(models.Model):
    value = models.CharField(max_length=100)
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.value


class Measure(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    levels = models.ManyToManyField(ProtectionLevel)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Sentence(models.Model):
    title = models.CharField(max_length=300)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE, related_name='sentences')
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE, related_name='sentences')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Cert(models.Model):
    name = models.CharField(max_length=300)
    date = models.CharField(max_length=300)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, related_name='sentences')
