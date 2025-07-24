from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'stylist', 'image_url', 'created_at')
    search_fields = ('stylist__name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    list_per_page = 25
