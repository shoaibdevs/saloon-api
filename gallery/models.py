from django.db import models

class Gallery(models.Model):
    stylist = models.ForeignKey(
        'stylists.Stylist',
        on_delete=models.CASCADE,
        related_name='galleries'
    )
    image_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery image by {self.stylist}"
