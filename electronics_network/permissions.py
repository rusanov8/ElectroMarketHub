from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Permission class to check the user's activity.

    Methods:
        - has_permission: Check if the user is active.

    """

    def has_permission(self, request, view):
        return request.user.is_active
