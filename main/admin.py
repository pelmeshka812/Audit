from django.contrib import admin

from main.models import Act, Product, Process, ProtectionLevel, Measure, DeviceType, Sentence

admin.site.register(Act)
admin.site.register(Product)
admin.site.register(Process)
admin.site.register(ProtectionLevel)
admin.site.register(Measure)
admin.site.register(DeviceType)
admin.site.register(Sentence)