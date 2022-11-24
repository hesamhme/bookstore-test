from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    national_id = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('book_list', args=[self.id])
