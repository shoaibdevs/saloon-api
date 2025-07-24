# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'role', 'is_active', 'is_staff', 'created_at')
    list_filter = ('role', 'is_active', 'is_staff', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Info', {
            'fields': ('email', 'full_name', 'phone', 'password')
        }),
        ('Role & Access', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Profile', {
            'fields': ('profile_image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone', 'role', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    def get_queryset(self, request):
        # Optional: customize queryset for superusers/admins
        return super().get_queryset(request)

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return f'<img src="{obj.profile_image.url}" width="50" height="50" />'
        return "No Image"
    profile_image_preview.allow_tags = True
    profile_image_preview.short_description = 'Profile Image'
