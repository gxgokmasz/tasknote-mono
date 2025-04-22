from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.base import View


@method_decorator(never_cache, "dispatch")
class LogoutView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponseNotAllowed(["GET"])

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        logout(request)

        return HttpResponseRedirect(reverse("login"))
