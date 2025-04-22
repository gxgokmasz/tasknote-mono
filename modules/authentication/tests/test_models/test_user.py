import pytest

from ...src.infrastructure.models import User


@pytest.mark.django_db(transaction=True)
def test_task_deactivation(create_user) -> None:
    user = User.objects.get(username="testuser_0")
    user.deactivate()

    actual_user_status = user.is_active
    expected_user_status = False

    assert actual_user_status == expected_user_status


@pytest.mark.django_db(transaction=True)
def test_task_activation(create_user) -> None:
    user = User.objects.get(username="testuser_0")
    user.deactivate()
    user.activate()

    actual_user_status = user.is_active
    expected_user_status = True

    assert actual_user_status == expected_user_status
