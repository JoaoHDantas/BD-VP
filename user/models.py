from django.db import models

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        return self.nickname if self.nickname else self.user.username