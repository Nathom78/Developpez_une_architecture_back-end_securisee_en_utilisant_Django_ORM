from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import MyUser
from .forms import UserCreationForm, UserChangeForm
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    readonly_fields = ["permissions"]

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'

    def permissions(self, user):
        # permissions = []
        # for permission in user.get_user_permissions():
        #     permissions.append(permission)
        return format_html_join(
            mark_safe("<br>"),
            "{}",
            ((line,) for line in user.get_group_permissions()),
        )

    permissions.short_description = 'permissions'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'role', 'email', 'is_active', 'is_staff', 'group', 'is_superuser')
    list_filter = ('role',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'permissions'), 'classes': ('collapse',)})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'email', 'password1', 'password2')
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)
