from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import json

# Create your models here.

class NewCampaign(models.Model):
    class Meta:
        managed = True

    CAMPAIGN_USE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=10, choices=CAMPAIGN_USE_CHOICES)
    user_info = models.TextField()
    purpose = models.TextField()
    target_audience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.name
    

class BusinessDomains(models.Model):
    class Meta:
        managed = True

    campaign = models.ForeignKey(NewCampaign, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=100, default="default_name")
    url = models.CharField(max_length=255, default="default_name")
    domain = models.CharField(max_length=255, default="default_name")
    content = models.TextField(default="None")
    # need to add finished flag


class NewBusinessDomains(models.Model):
    class Meta:
        managed = True
    campaign = models.ForeignKey(NewCampaign, on_delete=models.CASCADE, related_name='newbusinesses')
    name = models.CharField(max_length=100, default="default_name")
