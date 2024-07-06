from django.contrib import admin
from .models import ApiLog

@admin.register(ApiLog)
class ApiLogAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'status_code', 'duration', 'timestamp')
    list_filter = ('method', 'status_code')
    search_fields = ('path',)
