from rest_framework import permissions


class IsOwnerOrCustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS and obj.owner != request.user:
            return False
        return True