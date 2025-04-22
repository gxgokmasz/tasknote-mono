import pytest


@pytest.fixture()
def get_default_user_id():
    from modules.authentication.tests.factories import UserFactory

    user = UserFactory()

    yield user.id

    UserFactory.reset_sequence(0, True)
