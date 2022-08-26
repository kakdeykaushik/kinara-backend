from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Url(models.Model):

    short_url = models.CharField(max_length=30)
    original_url = models.TextField()
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveBigIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"OG - {self.original_url} && Short - {self.short_url}"
