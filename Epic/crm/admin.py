from django.contrib import admin

# Register your models here.

# from crm.models import (
#     Contributors,
#     Projects,
#     Issues,
#     Comments,
#     Users
# )


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
# admin.site.register(Contributors, ContributorsAdmin)
# admin.site.register(Projects, ProjectsAdmin)
# admin.site.register(Issues, IssuesAdmin)
# admin.site.register(Comments)
