from django.contrib import admin

from ..models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "is_done", "finish_date")
    list_per_page = 10

    fieldsets = (
        (
            "Informações da tarefa",
            {"fields": ("title", "description", "priority", "is_done", "user_id")},
        ),
        (
            "Datas importantes",
            {"fields": ("finish_date", "created_at", "updated_at", "deactivated_at")},
        ),
        ("Identificadores", {"fields": ("id", "public_id")}),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("title", "description", "priority", "is_done", "finish_date", "user_id")},
        ),
    )
    readonly_fields = ("id", "public_id", "user_id", "created_at", "updated_at", "deactivated_at")

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        return super().get_fieldsets(request, obj)
