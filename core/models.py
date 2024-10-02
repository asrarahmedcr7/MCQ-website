from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.username