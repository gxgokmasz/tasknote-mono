from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_not_authenticated_user_redirection(live_server, selenium_client) -> None:
    protected_url = live_server.url + reverse("task_list")
    login_url = live_server + reverse("login")
    selenium_client.get(protected_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = login_url

    assert actual_url == expected_url
