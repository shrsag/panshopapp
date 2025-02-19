# admin.py
from django.contrib import admin
from .models import Recipient

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Display name and email in the list view
    search_fields = ['name', 'email']  # Make name and email searchable
    list_filter = ['email']  # Optional: Add filtering options

# Register the model with the custom admin class
admin.site.register(Recipient, RecipientAdmin)

