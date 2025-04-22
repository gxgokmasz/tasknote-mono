import pytest

from ...src.infrastructure.models import Task


@pytest.mark.django_db(transaction=True)
def test_task_str_return(create_task) -> None:
    task = Task.objects.get(title="Task 0")

    actual_task_str_value = task.__str__()
    expected_task_str_value = "Task 0"

    assert actual_task_str_value == expected_task_str_value


@pytest.mark.django_db(transaction=True)
def test_task_deactivation(create_task) -> None:
    task = Task.objects.get(title="Task 0")
    task.deactivate()

    actual_task_status = not not task.deactivated_at
    expected_task_status = True

    assert actual_task_status == expected_task_status


@pytest.mark.django_db(transaction=True)
def test_task_activation(create_task) -> None:
    task = Task.objects.get(title="Task 0")
    task.deactivate()
    task.activate()

    actual_task_status = not not task.deactivated_at
    expected_task_status = False

    assert actual_task_status == expected_task_status
