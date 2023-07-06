from django.contrib import admin

from crm.models import (
    Contract,
    Event,
    Client
)


# class ContributorsAdmin(admin.ModelAdmin):
#     list_filter = [("project", admin.RelatedOnlyFieldListFilter)]
#     list_display = ["user", "project"]
#     ordering = ["project"]
#
#
# class IssuesAdmin(admin.ModelAdmin):
#     list_filter = ["status"]
#     list_display = ["title", "project", "status"]
#     ordering = ["project"]
#
#
# class ProjectsAdmin(admin.ModelAdmin):
#     readonly_fields = ('id',)

# And all models for personalized
admin.site.register(Client)
admin.site.register(Event)
admin.site.register(Contract)

