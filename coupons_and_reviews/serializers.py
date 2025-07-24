# serializers.py
from rest_framework import serializers
from .models import *

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    customer_name = serializers.StringRelatedField(source='customer', read_only=True)
    stylist_name = serializers.StringRelatedField(source='stylist', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['customer', 'created_at']


class AppliedCouponSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.full_name', read_only=True)
    coupon_code = serializers.CharField(source='coupon.code', read_only=True)
    appointment_id = serializers.IntegerField(source='appointment.id', read_only=True)

    class Meta:
        model = AppliedCoupon
        fields = [
            'id',
            'customer',          # For POST
            'customer_name',     # For display
            'coupon',            # For POST
            'coupon_code',       # For display
            'appointment',       # For POST
            'appointment_id',    # For display
            'applied_at'
        ]
        read_only_fields = ['id', 'applied_at']