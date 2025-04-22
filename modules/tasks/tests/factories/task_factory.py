import factory

from ...src.infrastructure.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: f"Task {n}")
    user_id = None

    class Meta:
        model = Task
        django_get_or_create = ("title",)
