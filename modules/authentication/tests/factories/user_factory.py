import factory

from ...src.infrastructure.models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"testuser_{n}")
    email = factory.Sequence(lambda n: f"testuser_{n}@email.com")
    password = factory.django.Password("strong-testpassword123")

    class Meta:
        model = User
        django_get_or_create = ("username", "email")
