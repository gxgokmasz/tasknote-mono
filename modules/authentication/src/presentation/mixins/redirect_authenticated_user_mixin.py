from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse


class RedirectAuthenticatedUserMixin:
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.session.get("user"):
            return HttpResponseRedirect(reverse("task_list"))

        return super().dispatch(request, *args, **kwargs)
