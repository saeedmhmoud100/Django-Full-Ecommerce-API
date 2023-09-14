from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user or request.user.is_superuser


class IsNotAdmin(IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return not super().has_object_permission(request,view,obj)


class IsNotAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return False
        return True


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)