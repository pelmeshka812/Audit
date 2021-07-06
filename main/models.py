from django.db import models


class Act(models.Model):
    name = models.CharField(max_length=250)


class Product(models.Model):
    name = models.CharField(max_length=250)


class Process(models.Model):
    identifier = models.CharField(max_length=6)
    name = models.CharField(max_length=250)
    act_id = models.ForeignKey(Act, on_delete=models.CASCADE)


class ProtectionLevel(models.Model):
    value = models.CharField(max_length=100)


class Measure(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    level = models.ForeignKey(ProtectionLevel, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)


class DeviceType(models.Model):
    name = models.CharField(max_length=250)


class Sentence(models.Model):
    sentence = models.CharField(max_length=300)
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
