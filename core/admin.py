from django.contrib import admin

from core.models import ActivityLog, Todo, Metricas


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')

class MetricasAdmin(admin.ModelAdmin):
    list_display = ('height', 'weight','gender','exercise')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Metricas)
