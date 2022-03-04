from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomerUser(AbstractUser):
    Tuoi = models.IntegerField(default=0)
    GioiTinh = models.CharField(max_length=10, null=True, blank=True)
    SDT = models.CharField(max_length=10, null=True, blank=True)