from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class Review(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    stylist = models.ForeignKey(
        'stylists.Stylist',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text='Rating should be between 1 and 5'
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} rated {self.stylist} - {self.rating}⭐"



class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveSmallIntegerField()
    discount_upto = models.PositiveSmallIntegerField(null=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-valid_to']


class AppliedCoupon(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='applied_coupons'
    )
    coupon = models.ForeignKey(
        Coupon, 
        on_delete=models.CASCADE, 
        related_name='applications'
    )
    appointment = models.ForeignKey(
        'appointments.Appointment', 
        on_delete=models.CASCADE, 
        related_name='coupon_applied'
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} used {self.coupon.code} on {self.appointment}"
