from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models import Value
from django.db.models.functions import Concat

import uuid


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25, verbose_name=_('first name'))
    last_name = models.CharField(max_length=25, verbose_name=_('last name'))
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=15, verbose_name=_('phone'))
    mobile = models.CharField(max_length=15)
    company_name = models.CharField(max_length=25, verbose_name=_('company name'))
    date_created = models.DateField(auto_now_add=True, verbose_name=_('date created'))
    date_updated = models.DateField(auto_now=True, verbose_name=_('date updated'))
    # contract = models.ForeignKey(to="Contract", on_delete=models.PROTECT)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('sales contact')
    )

    def full_name(self):
        return Concat(self.first_name, Value(" "), self.last_name)


class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('sales contact')
    )
    status = models.BooleanField(default=True, verbose_name=_('status'))
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name=_('client'))
    amount = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('amount'))
    payment_due = models.DateField(blank=True, null=True, verbose_name=_('payment due'))
    date_created = models.DateField(auto_now_add=True, verbose_name=_('date created'))
    date_updated = models.DateField(auto_now=True, verbose_name=_('date updated'))


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    support_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('support contact')
    )
    contract = models.OneToOneField(to=Contract, on_delete=models.CASCADE, verbose_name=_('contract'))
    event_status = Contract.status
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name=_('client'))
    attendees = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('attendees'))
    location = models.TextField(verbose_name=_('location'))
    note = models.TextField(verbose_name=_('note'))  # blank=True
    event_date = models.DateField(blank=True, null=True, verbose_name=_('event date'))
    date_created = models.DateField(auto_now_add=True, verbose_name=_('date created'))
    date_updated = models.DateField(auto_now=True, verbose_name=_('date updated'))
