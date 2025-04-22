import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("selenium_client", [{"authenticated": True}], indirect=True)
@pytest.mark.django_db(transaction=True)
def test_authenticated_user_login_url_redirection(
    live_server, create_user, selenium_client
) -> None:
    login_url = live_server.url + reverse("login")
    selenium_client.get(login_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "logout_button"))
    )
    tasks_list_url = live_server.url + reverse("task_list")

    actual_url = selenium_client.current_url
    expected_url = tasks_list_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_failed_user_authentication(live_server, selenium_client) -> None:
    login_url = live_server.url + reverse("login")
    selenium_client.get(login_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_password").send_keys("strong-testpassword123")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = login_url

    assert actual_url == expected_url


@pytest.mark.parametrize("selenium_client", [{"authenticated": True}], indirect=True)
@pytest.mark.django_db(transaction=True)
def test_successful_user_authentication(live_server, create_user, selenium_client) -> None:
    tasks_list_url = live_server.url + reverse("task_list")

    actual_url = selenium_client.current_url
    expected_url = tasks_list_url

    assert actual_url == expected_url
