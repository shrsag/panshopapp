from django.db import models

class Recipient(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)  # Store registered emails

    def __str__(self):
        return f"{self.name or 'Unnamed'} ({self.email})"
