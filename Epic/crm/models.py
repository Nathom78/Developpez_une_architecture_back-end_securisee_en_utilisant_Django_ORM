from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# settings.AUTH_USER_MODEL,
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    company_name = models.CharField(max_length=25)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField()
    contract = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
