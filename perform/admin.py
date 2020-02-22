from django.contrib import admin
from .models import PerformPost


@admin.register(PerformPost)
class PerformPostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'ip', 'author')
