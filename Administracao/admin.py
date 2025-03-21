from django.contrib import admin
from .models import SetoresCad

@admin.register(SetoresCad)
class SetoresCadAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
