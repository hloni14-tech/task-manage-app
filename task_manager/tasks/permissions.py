from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Manager').exists():
            return request.method in SAFE_METHODS or request.method == 'PUT'

        return obj.user == request.user
