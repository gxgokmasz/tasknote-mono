import inject
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
)
from django.urls import reverse
from django.views.generic.base import TemplateView

from ..mixins import TaskDetailMixin


class TaskDeactivateView(TaskDetailMixin, TemplateView):
    template_name = "pages/task_deactivate.html"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = self.get_context_data()

        task = context["task"]
        deactivate_task_use_case = inject.instance("DeactivateTaskUseCase")
        deactivate_task_use_case.execute(task.id)

        return HttpResponseRedirect(reverse("task_list"))
