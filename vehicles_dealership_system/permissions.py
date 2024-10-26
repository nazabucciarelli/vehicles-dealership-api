from rest_framework.permissions import BasePermission

class IsStaffForCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method in ['POST']:
            return request.user.is_authenticated and request.user.is_staff
        return False
    