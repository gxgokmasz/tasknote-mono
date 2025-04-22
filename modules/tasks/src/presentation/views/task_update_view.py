import inject
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from ...application.dtos import TaskUpdateDTO
from ...infrastructure.htmx.http import HttpRequest
from ...presentation.forms.task_form import TaskForm
from ..mixins import TaskDetailMixin


class TaskUpdateView(TaskDetailMixin, FormView):
    form_class = TaskForm
    template_name = "pages/task_update.html"

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        context = self.get_context_data()

        task = context["task"]
        update_task_path = reverse("task_update", kwargs={"public_id": task.public_id})

        if request.htmx.current_url_abs_path == update_task_path:
            form = self.get_form()

            if form.is_valid():
                cleaned_data = form.cleaned_data

                task_to_update = TaskUpdateDTO(
                    task.id,
                    cleaned_data["title"],
                    cleaned_data["priority"],
                    cleaned_data["description"],
                    cleaned_data["finish_date"],
                )
                update_task_use_case = inject.instance("UpdateTaskUseCase")
                update_task_use_case.execute(task_to_update)

            return render(
                self.request, "partials/task_update_form_inputs.html", self.get_context_data()
            )

        toggle_task_done_use_case = inject.instance("ToggleTaskDoneUseCase")
        toggle_task_done_use_case.execute(task.id)

        return render(request, "partials/task_card_details.html", self.get_context_data())
