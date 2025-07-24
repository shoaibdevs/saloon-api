from rest_framework.permissions import BasePermission, SAFE_METHODS
import datetime

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class IsAdminOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
    

    
class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.customer == request.user or request.user.is_superuser


class IsAdminToDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method != 'DELETE' or request.user.is_superuser
    

    
