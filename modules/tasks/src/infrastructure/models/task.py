import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    public_id = models.UUIDField(
        _("id público"), unique=True, db_index=True, editable=False, default=uuid.uuid4
    )

    title = models.CharField(_("título"), max_length=64)
    description = models.TextField(_("descrição"), blank=True, null=True)
    is_done = models.BooleanField(_("está feito"), default=False)

    user_id = models.PositiveIntegerField(_("ID do usuário"))

    created_at = models.DateTimeField(_("data de criação"), auto_now_add=True)
    updated_at = models.DateTimeField(_("data de atualização"), auto_now=True)
    deactivated_at = models.DateTimeField(_("data de desativação"), blank=True, null=True)

    class TaskPriorities(models.IntegerChoices):
        HIGH = 1, _("alta")
        MEDIUM = 2, _("média")
        LOW = 3, _("baixa")

    priority = models.IntegerField(
        _("prioridade"), choices=TaskPriorities, default=TaskPriorities.HIGH
    )

    finish_date = models.DateField(_("data de finalização"), blank=True, null=True)

    class Meta:
        ordering = ["priority"]

    def __str__(self) -> str:
        return self.title

    def deactivate(self):
        self.deactivated_at = timezone.now()
        self.save()

    def activate(self):
        self.deactivated_at = None
        self.save()
