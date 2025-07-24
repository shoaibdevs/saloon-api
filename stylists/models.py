from django.db import models
from django.conf import settings



class Stylist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stylist_profile')
    bio = models.TextField(blank=True)
    specialization = models.TextField(blank=True)
    skills = models.TextField(blank=True, help_text="Comma-separated list, e.g., Haircut,Coloring")
    experience_years = models.PositiveIntegerField()
    rating_avg = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    available_days = models.CharField(max_length=50, help_text="e.g., Mon,Tue,Thu")
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user.full_name} - {self.specialization}"
