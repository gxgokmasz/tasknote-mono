from django.urls import path

from .views import (
    DailyTaskListView,
    TaskCreateView,
    TaskDeactivateView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tasks/daily/", DailyTaskListView.as_view(), name="task_daily"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/update/<slug:public_id>/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/delete/<slug:public_id>/", TaskDeactivateView.as_view(), name="task_delete"),
]
