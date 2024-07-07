from django.db import models

class Transaction(models.Model):
    text = models.TextField()
    prediction = models.CharField(max_length=100)

    def __str__(self):
        return self.text[:50]  # Show the first 50 characters in the admin interface
