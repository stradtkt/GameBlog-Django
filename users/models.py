from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

