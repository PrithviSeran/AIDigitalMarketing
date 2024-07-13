from django.db import models
#from django.contrib.auth.models import User
import json

# Create your models here.
class Campaign(models.Model):
    class Meta:
        managed = True

    CAMPAIGN_USE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=10, choices=CAMPAIGN_USE_CHOICES)
    user_info = models.TextField()
    purpose = models.TextField()
    target_audience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class BusinessDomains(models.Model):
    class Meta:
        managed = True
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=100, default="default_name")


class NewBusinessDomains(models.Model):
    class Meta:
        managed = True
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='newbusinesses')
    name = models.CharField(max_length=100, default="default_name")
