import pytest

from ..factories import TaskFactory


@pytest.fixture
def create_task(get_default_user_id):
    task = TaskFactory(user_id=get_default_user_id)

    yield task

    TaskFactory.reset_sequence(0, True)
