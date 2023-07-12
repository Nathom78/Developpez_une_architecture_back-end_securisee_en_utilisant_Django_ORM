from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db.models import Value
from django.db.models.functions import Concat

import uuid


def status_contract_update():
    status = models.Sum("Event.event_status", distinct=True, default=False)
    return status


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
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('sales contact')
    )
    existing = models.BooleanField(default=False, verbose_name=_('existing'))
    note = models.TextField(blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


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

    def save(self, *args, **kwargs):
        all_event = Event.objects.filter(contract=self).values('event_status')
        if all_event:
            nb_truth = all_event.filter(contract=self).filter(event_status=True).count()
            self.status = True if nb_truth > 0 else False
        super().save(*args, **kwargs)

    def __str__(self):
        name = _('Contract')
        client_name = Client.objects.get(pk=self.client.pk)
        return f"{name}: {client_name.full_name} du {self.date_created}"


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    support_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('support contact')
    )
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, verbose_name=_('contract'))
    event_status = models.BooleanField(default=True, verbose_name=_('status'))
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name=_('client'))
    attendees = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('attendees'))
    location = models.TextField(verbose_name=_('location'), blank=True)
    note = models.TextField(verbose_name=_('note'), blank=True)
    event_date = models.DateField(blank=True, null=True, verbose_name=_('event date'))
    date_created = models.DateField(auto_now_add=True, verbose_name=_('date created'))
    date_updated = models.DateField(auto_now=True, verbose_name=_('date updated'))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        contract_to_update = Contract.objects.get(pk=self.contract.pk)
        contract_to_update.save()

    def __str__(self):
        name = _('Event')
        client_name = Client.objects.get(pk=self.client.pk)
        return f"{name}: {client_name.full_name} {self.event_date}"