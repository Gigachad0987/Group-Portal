from django.db import models
from django.contrib.auth.models import User
class Announcements(models.Model):
    title = models.TextField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    def __str__(self):
        return self.title