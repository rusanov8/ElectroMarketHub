from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
        Permission class to check if the user is a superuser.

        Methods:
            - has_permission: Check if the user is a superuser.

    """

    def has_permission(self, request, view):
        return request.user.is_superuser

