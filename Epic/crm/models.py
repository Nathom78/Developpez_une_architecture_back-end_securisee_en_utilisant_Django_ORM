from django.db import models
from django.conf import settings
from django.contrib import admin
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _, gettext

import uuid


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(verbose_name=_("first name"), max_length=25)
    last_name = models.CharField(verbose_name=_("last name"), max_length=25)
    email = models.EmailField(verbose_name=_("email address"), max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(verbose_name=_("office phone"), max_length=15, blank=True)
    mobile = models.CharField(verbose_name=_("mobile"), max_length=15, blank=True)
    company_name = models.CharField(verbose_name=_("company name"), max_length=25)
    sales_contact = models.ForeignKey(verbose_name=_("sales contact"), to=settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT
                                      )
    existing = models.BooleanField(verbose_name=_("existing"), default=False)
    note = models.TextField(verbose_name=_("note"), blank=True)
    date_created = models.DateField(verbose_name=_("date created"), auto_now_add=True, editable=False)
    date_updated = models.DateField(verbose_name=_("date updated"), auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    class Meta:
        constraints = [UniqueConstraint(name="unique_full_name", fields=["first_name", "last_name", "company_name"])]


class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.BooleanField(default=True, verbose_name=_("status"))
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, limit_choices_to={"existing": True},
                               verbose_name=_("client"))
    amount = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("amount"))
    payment_due = models.DateField(blank=True, null=True, verbose_name=_("payment due"))
    date_created = models.DateField(auto_now_add=True, verbose_name=_("date created"), editable=False)
    date_updated = models.DateField(auto_now=True, verbose_name=_("date updated"))

    def save(self, *args, **kwargs):
        all_event = Event.objects.filter(contract=self).values("event_status")
        if all_event:
            nb_truth = all_event.filter(contract=self).filter(event_status=True).count()
            self.status = True if nb_truth > 0 else False
        super().save(*args, **kwargs)

    @property
    def contract_name(self):
        name = gettext("Contract")
        on = gettext("of")
        client_name = Client.objects.get(pk=self.client.pk)
        return f"{name}: {client_name.full_name} {on} {self.date_created}"

    def __str__(self):
        return str(self.contract_name)

    @property
    @admin.display(description=_("sales contact"))
    def sales_contact(self):
        return Client.objects.get(pk=self.client.pk).sales_contact

    class Meta:
        constraints = [UniqueConstraint(name="unique_contract_by_day", fields=["client", "date_created"])]


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    support_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT,
                                     verbose_name=_("support contact"))
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, verbose_name=_("contract"))
    event_status = models.BooleanField(default=True, verbose_name=_("status"))
    attendees = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("attendees"))
    location = models.TextField(verbose_name=_("location"), blank=True)
    note = models.TextField(verbose_name=_("note"), blank=True)
    event_date = models.DateField(blank=True, null=True, verbose_name=_("event date"))
    date_created = models.DateField(auto_now_add=True, verbose_name=_("date created"), editable=False)
    date_updated = models.DateField(auto_now=True, verbose_name=_("date updated"))

    def save(self, *args, **kwargs):
        """For updated the Contract status"""
        contract_to_update = Contract.objects.get(pk=self.contract.pk)
        contract_to_update.save()
        super().save(*args, **kwargs)

    def __str__(self):
        name = gettext("Event")
        on = gettext("of")
        client_name = Contract.objects.get(pk=self.contract.pk).client
        return f"{name}: {client_name} {on} {self.event_date if self.event_date is not None else ''}"

    @property
    @admin.display(description=_("client"))
    def client(self):
        return Contract.objects.get(pk=self.contract.pk).client
