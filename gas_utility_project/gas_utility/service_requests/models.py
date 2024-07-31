from django.db import models


class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
    ]

    request_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.request_type} - {self.created_at}"
