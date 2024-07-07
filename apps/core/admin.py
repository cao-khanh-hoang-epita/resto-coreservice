from django.contrib import admin
from .models import RestoTable

@admin.register(RestoTable)
class RestoTableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_occupied', 'created_at', 'updated_at')
    list_filter = ('is_occupied',)
    search_fields = ('table_number',)
