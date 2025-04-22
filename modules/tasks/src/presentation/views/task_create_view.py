import inject
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from ...application.dtos import TaskCreateDTO
from ..forms import TaskForm
from ..mixins import AuthenticatedUserMixin


class TaskCreateView(AuthenticatedUserMixin, FormView):
    form_class = TaskForm
    template_name = "pages/task_create.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form: TaskForm) -> HttpResponse:
        cleaned_data = form.cleaned_data

        logged_in_user = self.get_logged_in_user()

        task = TaskCreateDTO(
            cleaned_data["title"],
            logged_in_user["id"],
            cleaned_data.get("priority"),
            cleaned_data.get("description"),
            cleaned_data.get("finish_date"),
        )
        create_task_use_case = inject.instance("CreateTaskUseCase")
        create_task_use_case.execute(task)

        return super().form_valid(form)
