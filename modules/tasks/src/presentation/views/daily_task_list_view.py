from django.views.generic.base import TemplateView

from ..mixins import DateProcessingMixin, TaskQuerysetMixin


class DailyTaskListView(TaskQuerysetMixin, DateProcessingMixin, TemplateView):
    template_name = "pages/task_daily_list.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        today = self.get_today()

        active_tasks = self.get_active_tasks()
        daily_tasks = [task for task in active_tasks if task.finish_date == today]
        task_priorities = list(dict.fromkeys([task.priority for task in daily_tasks]))

        context.update({"tasks": daily_tasks, "priorities": task_priorities})

        return context
