from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    creat_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Perfil de {self.username}'
