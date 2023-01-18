from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


class IsOwnerCheckMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("users:login")
        if self.get_object().user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


