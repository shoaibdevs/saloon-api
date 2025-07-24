from django.db import models
from django.conf import settings
import uuid
import datetime

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    stylist = models.ForeignKey('stylists.Stylist', on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.appointment_date} at {self.appointment_time}"
    
    @property
    def datetime(self):
        return datetime.datetime.combine(self.appointment_date, self.appointment_time)
    
    @property
    def is_cancelable(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        return (self.datetime.replace(tzinfo=datetime.timezone.utc) - now).total_seconds() > 86400 and self.status == 'confirmed'