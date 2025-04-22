import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_get_logout_url(client) -> None:
    logout_url = reverse("logout")
    response = client.get(logout_url)

    actual_status_code = response.status_code
    expected_status_code = 405

    assert actual_status_code == expected_status_code


@pytest.mark.parametrize(
    "selenium_client",
    [{"authenticated": True, "username": "testuser_0", "password": "strong-testpassword123"}],
    indirect=True,
)
@pytest.mark.django_db(transaction=True)
def test_successful_logout(live_server, create_user, selenium_client) -> None:
    login_url = live_server + reverse("login")
    selenium_client.find_element(value="logout_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = login_url

    assert actual_url == expected_url
