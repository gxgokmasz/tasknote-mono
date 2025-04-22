from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from ...presentation.forms import UserCreationForm
from ..models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ("username", "email", "is_staff")
    list_per_page = 10

    fieldsets = (
        ("Informações do usuário", {"fields": ("username", "password", "email")}),
        (
            "Permissões",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        (
            "Datas importantes",
            {"fields": ("date_joined", "updated_at", "last_login", "deactivated_at")},
        ),
        ("Identificadores", {"fields": ("id", "public_id")}),
    )
    add_fieldsets = ((None, {"fields": ("username", "email", "password1", "password2")}),)
    readonly_fields = (
        "id",
        "public_id",
        "is_active",
        "date_joined",
        "updated_at",
        "last_login",
        "deactivated_at",
    )

    add_form = UserCreationForm
