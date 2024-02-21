from django.db import models
from django.urls import reverse

class Event(models.Model):
    title           = models.CharField(max_length=255, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    image           = models.ImageField(upload_to='imgs/', blank=True, null=True)
    start_date      = models.DateTimeField()
    end_date        = models.DateTimeField()
    location        = models.CharField(max_length=255)
    url_link        = models.URLField()
    cost            = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    event_type      = models.CharField(max_length=255, blank=True, null=True)
    event_category  = models.CharField(max_length=255, blank=True, null=True)
    views           = models.IntegerField(default=0) 
    is_featured     = models.BooleanField(default=False, blank=True, null=True)
    created         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name  = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
