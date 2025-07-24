from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'stylist', 'service', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_date', 'stylist')
    search_fields = ('customer__full_name', 'stylist__user__full_name', 'service__name')
    ordering = ('-appointment_date', 'appointment_time')
