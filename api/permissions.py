from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to have full access.
    Non-admin users can only perform GET requests.
    """

    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow full access only to admin users
        return request.user and request.user.is_staff
