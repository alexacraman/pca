from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.email}, approved {self.is_approved}"
    
    def get_absolute_url(self):
        return reverse('accounts:user-profile', kwargs={'id': self.id})
    

class CommitteeMembers(models.Model):
    member_name = models.CharField(max_length=150, blank=True, null=True)
    position    = models.CharField(max_length=50,  blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    image       = models.ImageField(upload_to='img/committee/', blank=True, null=True)

    def __str__(self):
        return self.member_name
    
    def get_absolute_url(self):
        return reverse('accounts:committee-members-detail', kwargs={'pk': self.pk})


