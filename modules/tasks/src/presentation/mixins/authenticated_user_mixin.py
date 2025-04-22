from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse


class AuthenticatedUserMixin:
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.session.get("user") is None:
            return HttpResponseRedirect(reverse("login"))

        return super().dispatch(request, *args, **kwargs)

    def get_logged_in_user(self) -> dict:
        return self.request.session["user"]
