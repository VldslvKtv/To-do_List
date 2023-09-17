from django.contrib import admin
from .models import Record


class ToDoAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Record, ToDoAdmin)
