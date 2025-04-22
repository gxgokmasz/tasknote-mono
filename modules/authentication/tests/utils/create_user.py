import pytest

from ..factories import UserFactory


@pytest.fixture
def create_user():
    user = UserFactory()

    yield user

    UserFactory.reset_sequence(0, True)
