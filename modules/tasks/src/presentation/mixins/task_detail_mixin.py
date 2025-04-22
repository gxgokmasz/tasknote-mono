import inject
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseNotFound

from .authenticated_user_mixin import AuthenticatedUserMixin


class TaskDetailMixin(AuthenticatedUserMixin):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = self.get_context_data()

        task = context["task"]

        logged_in_user = self.get_logged_in_user()

        if task.user_id is not logged_in_user["id"]:
            return HttpResponseForbidden()

        if task.deactivated_at is not None:
            return HttpResponseNotFound()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        public_id = self.kwargs["public_id"]

        get_task_use_case = inject.instance("GetTaskUseCase")
        task = get_task_use_case.execute(public_id)

        if task:
            context.update({"task": task})

        return context
