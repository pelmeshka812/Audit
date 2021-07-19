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
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Process(models.Model):
    identifier = models.CharField(max_length=6, blank=True)
    name = models.CharField(max_length=250)
    subprocess = models.ManyToManyField(SubProcess)

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
    level = models.ForeignKey(ProtectionLevel, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Sentence(models.Model):
    sentence = models.CharField(max_length=300)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.sentence
