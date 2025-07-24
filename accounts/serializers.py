from rest_framework import serializers

from stylists.models import Stylist
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'email',
            'phone',
            'role',
            'profile_image',
            'is_active',
            'created_at',
            'updated_at',
        ]

class StylistSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    email = serializers.EmailField(source='user.email')
    phone = serializers.CharField(source='user.phone')
    profile_image = serializers.ImageField(source='user.profile_image')

    class Meta:
        model = Stylist
        fields = [
            'full_name', 'email', 'phone', 'profile_image',
            'bio', 'specialization', 'experience_years',
            'rating_avg', 'available_days', 'start_time', 'end_time'
        ]