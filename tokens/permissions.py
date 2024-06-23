from rest_framework import permissions

class IsOwnerOfUser(permissions.BasePermission):
    def has_object_permission(self, request, obj, view):
        return obj.username == request.user.username  