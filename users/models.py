from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.



class User(AbstractUser):

    username = models.CharField(max_length=20, unique=True, blank=False, null=False)


    def get_token(self):
        token = Token.objects.get(user=self)
        return token


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Token.objects.create(user=self)

