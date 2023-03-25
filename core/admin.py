from django.contrib import admin

from core.models import ActivityLog, Metricas, Cerveja, Cervejada


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class CervejadaAdmin(admin.ModelAdmin):
    list_display = ('qntd_cervejas', 'tempo_corrida', 'done')

class MetricasAdmin(admin.ModelAdmin):
    list_display = ('height', 'weight','gender','exercise')

class CervejaAdmin(admin.ModelAdmin):
    list_display = ('marca', 'mls','valor_calorico')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Cervejada, CervejadaAdmin)
admin.site.register(Metricas, MetricasAdmin)
admin.site.register(Cerveja, CervejaAdmin)

