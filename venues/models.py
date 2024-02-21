from django.db import models
from django.urls import reverse

class Venue(models.Model):
    name        = models.CharField(max_length=100)
    address     = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone       = models.CharField(max_length=50, blank=True, null=True)
    email       = models.EmailField(blank=True, null=True)
    website     = models.URLField(blank=True, null=True)
    latitude    = models.DecimalField(max_digits=25, decimal_places=16, blank=True, null=True)
    longitude   = models.DecimalField(max_digits=25, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('venues:venue-detail', kwargs={'pk' : self.pk})
