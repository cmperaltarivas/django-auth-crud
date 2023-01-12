from django.contrib import admin
from .models import Task

#pasar campos de solo lectura que no se pueden modificar a la vista admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
# Register your models here.
admin.site.register(Task,TaskAdmin)