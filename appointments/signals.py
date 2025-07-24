# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from notifications.models import Notification  # your notification model


@receiver(post_save, sender=Appointment)
def notify_on_appointment_change(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.stylist.user,
            message=f"New appointment booked by {instance.customer.full_name}"
        )
    elif instance.status == 'confirmed':
        Notification.objects.create(
            user=instance.customer,
            message=f"Your appointment with {instance.stylist} is confirmed!"
        )
    elif instance.status == 'cancelled':
        Notification.objects.create(
            user=instance.customer,
            message=f"Your appointment with {instance.stylist} has been cancelled."
        )
