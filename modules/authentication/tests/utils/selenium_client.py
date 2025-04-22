import pytest
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def selenium_client(live_server, request):
    defaults = {
        "authenticated": False,
        "headless": True,
        "username": "testuser_0",
        "password": "strong-testpassword123",
    }

    params = defaults.copy()

    if hasattr(request, "param"):
        params.update(request.param)

    chrome_options = webdriver.ChromeOptions()

    if params["headless"]:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=chrome_options)

    browser.implicitly_wait(10)

    if params["authenticated"]:
        browser.get(live_server.url + reverse("login"))
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
        browser.find_element(value="id_username").send_keys(params["username"])
        browser.find_element(value="id_password").send_keys(params["password"])
        browser.find_element(value="submit_button").click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "logout_button")))

    yield browser

    browser.quit()
