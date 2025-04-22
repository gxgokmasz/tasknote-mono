import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    public_id = models.UUIDField(
        _("id público"), unique=True, db_index=True, editable=False, default=uuid.uuid4
    )

    email = models.EmailField(_("endereço de email"), unique=True, db_index=True)

    updated_at = models.DateTimeField(_("data de atualização"), auto_now=True)
    deactivated_at = models.DateTimeField(_("data de desativação"), blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        ordering = ["-date_joined"]

    def deactivate(self) -> None:
        self.deactivated_at = timezone.now()
        self.is_active = False
        self.save()

    def activate(self) -> None:
        self.deactivated_at = None
        self.is_active = True
        self.save()
