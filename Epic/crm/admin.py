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

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.sales_contact:
                return False
        return request.user.has_perm('crm.change_client')


class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_status", "contract"]
    ordering = ["event_date"]
    search_fields = ["client__last_name", "client__company_name"]
    empty_value_display = ""

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.support_user:
                return False
        return request.user.has_perm('crm.change_event')


class EventInline(admin.StackedInline):
    model = Event
    extra = 0


class ContractAdmin(admin.ModelAdmin):
    list_display = ["__str__", "client", "status"]
    ordering = ["client"]
    search_fields = ["client__last_name", "client__company_name"]
    inlines = [EventInline, ]

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.sales_contact:
                return False
        return request.user.has_perm('crm.change_contract')


# class ProjectsAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)

# And all models for personalized
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)
