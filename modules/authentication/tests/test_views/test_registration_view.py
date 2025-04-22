import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...src.infrastructure.models import User


@pytest.mark.parametrize("selenium_client", [{"authenticated": True}], indirect=True)
@pytest.mark.django_db(transaction=True)
def test_authenticated_user_registration_url_redirection(
    live_server, create_user, selenium_client
) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "logout_button"))
    )
    tasks_list_url = live_server.url + reverse("task_list")

    actual_url = selenium_client.current_url
    expected_url = tasks_list_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_successful_user_creation(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("strong-testpassword123")
    selenium_client.find_element(value="id_password2").send_keys("strong-testpassword123")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "logout_button"))
    )
    created_user = User.objects.get(email="testuser_0@email.com")

    actual_created_user_username = created_user.username
    expected_created_user_username = "testuser_0"

    assert actual_created_user_username == expected_created_user_username
