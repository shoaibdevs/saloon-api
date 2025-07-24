from rest_framework import serializers
from .models import Stylist
from accounts.serializers import UserSerializer 

class StylistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Stylist
        fields = [
            'id',
            'user',
            'bio',
            'specialization',
            'skills',
            'experience_years',
            'rating_avg',
            'available_days',
            'start_time',
            'end_time'
        ]
