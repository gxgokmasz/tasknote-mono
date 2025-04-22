from datetime import date

from django.views.generic.base import TemplateView

from ..mixins import DateProcessingMixin, TaskQuerysetMixin


class TaskListView(TaskQuerysetMixin, DateProcessingMixin, TemplateView):
    template_name = "pages/task_list.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        today = self.get_today()

        active_tasks = self.get_active_tasks()
        ordered_tasks = sorted(
            active_tasks,
            key=lambda task: (task.finish_date or date.min, -task.priority, task.title),
            reverse=True,
        )
        task_dates = list(dict.fromkeys(task.finish_date for task in ordered_tasks))
        task_out_dates = self.get_outdated_dates(task_dates, today)

        context.update(
            {
                "tasks": ordered_tasks,
                "dates": task_dates,
                "out_dates": task_out_dates,
                "today": today,
            }
        )

        return context
