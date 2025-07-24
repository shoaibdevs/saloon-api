from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message_short', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')
    ordering = ('-created_at',)
    list_per_page = 25

    def message_short(self, obj):
        return (obj.message[:50] + '...') if len(obj.message) > 50 else obj.message
    message_short.short_description = 'Message'
