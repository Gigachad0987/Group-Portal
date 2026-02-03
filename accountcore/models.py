from django.db import models
from django.contrib.auth.models import User

class GroupProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="group_logos/", null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="user_avatar/", null=True, blank=True)
    bio = models.TextField()
    rols = [
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("member", "Member")
    ]
    role = models.CharField(max_length=50, choices=rols, default="member")
    def __str__(self):
        return self.user.username