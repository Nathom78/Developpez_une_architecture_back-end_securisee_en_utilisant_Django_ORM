# CRM permissions
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _


class IsContactOrAuthenticated(BasePermission):
    message = _('User is not the team contact or not authenticated ')

    def has_permission(self, request, view):
        """
        For the list, just need the authentication to return True.
        With complement for others with object permissions.
        """
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """
        For retrieve just need the authentication,
        for other need to be the contact team for editing.
        """
        if view.__class__.__name__ == "EventViewSet":
            if request.user == obj.contract.sales_contact:
                return True
            contact = obj.support_user
        else:
            contact = obj.sales_contact
        return bool(request.method == 'GET' or request.user == contact or request.user.role == 'administrator')
