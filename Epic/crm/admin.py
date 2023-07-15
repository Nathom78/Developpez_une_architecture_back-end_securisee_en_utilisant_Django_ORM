from django.contrib import admin

from crm.models import (
    Contract,
    Event,
    Client
)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["__str__", "company_name", "existing"]
    search_fields = ["last_name"]
    ordering = ["last_name"]


class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_status", "contract"]
    ordering = ["event_date"]
    search_fields = ["client__last_name", "client__company_name"]
    empty_value_display = ""


class ContractAdmin(admin.ModelAdmin):
    list_display = ["__str__", "client", "status"]
    ordering = ["client"]
    search_fields = ["client__last_name", "client__company_name"]


# class ProjectsAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)

# And all models for personalized
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)
