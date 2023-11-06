from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticated):
    """
    Custom permission to allow only authenticated users to create, update, or delete objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)
