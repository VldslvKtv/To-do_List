from django.contrib import admin
from .models import Record


class ToDoAdmin(admin.ModelAdmin):
    read_only = ('date',)


admin.site.register(Record, ToDoAdmin)
