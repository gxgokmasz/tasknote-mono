import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.django_db(transaction=True)
def test_different_password_form_error(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("strong-testpassword123")
    selenium_client.find_element(value="id_password2").send_keys(
        "strong-testpassword123-different"
    )
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_numeric_password_form_error(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("12345678")
    selenium_client.find_element(value="id_password2").send_keys("12345678")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_user_similarity_password_form_error(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("testuser_0123")
    selenium_client.find_element(value="id_password2").send_keys("testuser_0123")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_common_password_form_error(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("password123")
    selenium_client.find_element(value="id_password2").send_keys("password123")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_minimum_length_password_form_error(live_server, selenium_client) -> None:
    registration_url = live_server.url + reverse("register")
    selenium_client.get(registration_url)
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    selenium_client.find_element(value="id_username").send_keys("testuser_0")
    selenium_client.find_element(value="id_email").send_keys("testuser_0@email.com")
    selenium_client.find_element(value="id_password1").send_keys("strong-")
    selenium_client.find_element(value="id_password2").send_keys("strong-")
    selenium_client.find_element(value="submit_button").click()
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url


@pytest.mark.django_db(transaction=True)
def test_registered_username_email_form_error(live_server, create_user, selenium_client) -> None:
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
        EC.presence_of_element_located((By.ID, "id_username"))
    )

    actual_url = selenium_client.current_url
    expected_url = registration_url

    assert actual_url == expected_url
