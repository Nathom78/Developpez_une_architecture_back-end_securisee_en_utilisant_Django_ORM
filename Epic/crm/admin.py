from django.contrib import admin

from crm.models import (
    Contract,
    Event,
    Client
)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["__str__", "company_name", "existing"]
    search_fields = ["^last_name"]
    ordering = ["last_name"]
    readonly_fields = ["date_created", "date_updated"]

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.sales_contact and not request.user.groups.filter(name='administrator').exists():
                return False
        return request.user.has_perm('crm.change_client')


class EventAdmin(admin.ModelAdmin):
    list_display = ["__str__", "event_status", "contract"]
    ordering = ["event_date"]
    search_fields = ["^support_user__username", "contract__id", "id"]
    empty_value_display = ""
    readonly_fields = ["client", "date_created", "date_updated"]
    fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ["support_user", "client", "contract", "event_status", "attendees", "location", "note",
                       "event_date", "date_created", "date_updated"]
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ["support_user", "contract", "event_status", "attendees", "location", "note", "event_date"]
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.support_user and request.user != obj.contract.sales_contact \
                    and not request.user.groups.filter(name='administrator').exists():
                return False
        return request.user.has_perm('crm.change_event')


class EventInline(admin.StackedInline):
    model = Event
    extra = 0
    readonly_fields = ["client", "date_created", "date_updated"]
    fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ["support_user", "client", "contract", "event_status", "attendees", "location", "note",
                       "event_date", "date_created", "date_updated"]
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ["support_user", "contract", "event_status", "attendees", "location", "note", "event_date"]
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


class ContractAdmin(admin.ModelAdmin):
    list_display = ["__str__", "client", "status"]
    ordering = ["client"]
    search_fields = ["^client__last_name", "^client__company_name", "id"]
    inlines = [EventInline, ]
    save_on_top = True
    readonly_fields = ["sales_contact", "date_created", "date_updated"]
    fields = ["status", "sales_contact", "client", "amount", "payment_due", "date_created", "date_updated"]

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user != obj.sales_contact and not request.user.groups.filter(name='administrator').exists():
                return False
        return request.user.has_perm('crm.change_contract')


# And all models for personalized
admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)
