from rest_framework import serializers
from .models import Appointment
from accounts.serializers import UserSerializer  # adjust as per your setup
from stylists.serializers import StylistSerializer
from services.serializers import ServiceSerializer
from stylists.models import Stylist
from services.models import Service

class AppointmentSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    stylist = StylistSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)
    stylist_id = serializers.PrimaryKeyRelatedField(
        queryset=Stylist.objects.all(), write_only=True
    )
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), write_only=True
    )
    # Computed fields
    is_cancelable = serializers.ReadOnlyField()
    datetime = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        fields = [
            'id',
            'customer',
            'stylist',
            'stylist_id',
            'service_id',
            'service',
            'appointment_date',
            'appointment_time',
            'status',
            'note',
            'created_at',
            'datetime',
            'is_cancelable',
        ]
