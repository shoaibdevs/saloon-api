from django.contrib import admin
from .models import Stylist

@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience_years', 'rating_avg', 'available_days', 'start_time', 'end_time')
    list_filter = ('specialization', 'available_days')
    search_fields = ('user__full_name', 'specialization')
