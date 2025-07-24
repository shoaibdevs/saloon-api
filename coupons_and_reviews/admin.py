from django.contrib import admin
from .models import Review, Coupon, AppliedCoupon


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'stylist', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'stylist')
    search_fields = ('customer__username', 'stylist__name', 'comment')
    ordering = ('-created_at',)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'discount_percent', 'valid_from', 'valid_to', 'is_active')
    list_filter = ('is_active', 'valid_from', 'valid_to')
    search_fields = ('code',)
    ordering = ('-valid_to',)


@admin.register(AppliedCoupon)
class AppliedCouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'coupon', 'appointment', 'applied_at')
    list_filter = ('applied_at', 'coupon')
    search_fields = ('customer__username', 'coupon__code', 'appointment__id')
    ordering = ('-applied_at',)
    autocomplete_fields = ('customer', 'coupon', 'appointment')
