from django.contrib import admin

from main.models import Act, Product, Process, ProtectionLevel, Measure, DeviceType, Sentence, SubProcess


# admin.site.register(Act)
# admin.site.register(Product)
# admin.site.register(Process)
# admin.site.register(ProtectionLevel)
# admin.site.register(Measure)
# admin.site.register(DeviceType)
# admin.site.register(Sentence)


@admin.register(Act)
class ActAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name',)


@admin.register(SubProcess)
class SubProcessAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name',)


@admin.register(ProtectionLevel)
class ProtectionLevelAdmin(admin.ModelAdmin):
    list_display = ('value', 'act_id')


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    def get_level(self, obj):
        return "\n".join([p.level for p in obj.level.all()])


@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('sentence', 'type', 'measure', 'description',)
