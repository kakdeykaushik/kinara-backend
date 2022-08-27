from django.db import models
from django.contrib.auth import get_user_model
import random
User = get_user_model()

class Url(models.Model):

    short_url = models.CharField(max_length=30)
    original_url = models.TextField()
    is_active = models.BooleanField(default=True)
    clicks = models.PositiveBigIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



    def generate_short_url(self):
        CORPUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        while True:
            mini_url = ""
            for _ in range(7):
                mini_url += random.choice(CORPUS)

            if not Url.objects.filter(short_url=mini_url).exists():
                break

        return mini_url


    def save(self, *args, **kwargs):
        self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"OG - {self.original_url} && Short - {self.short_url}"
