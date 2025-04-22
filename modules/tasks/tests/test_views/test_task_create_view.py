import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...src.infrastructure.models import Task


@pytest.mark.parametrize("selenium_client", [{"authenticated": True}], indirect=True)
@pytest.mark.django_db(transaction=True)
def test_successful_task_creation(live_server, create_task, selenium_client) -> None:
    task_create_url = live_server.url + reverse("task_create")
    selenium_client.get(task_create_url)
    WebDriverWait(selenium_client, 10).until(EC.presence_of_element_located((By.ID, "id_title")))
    selenium_client.find_element(value="id_title").send_keys("Task 1")
    selenium_client.find_element(value="submit_button").click()
    pre_created_task = Task.objects.get(title="Task 0")
    WebDriverWait(selenium_client, 10).until(
        EC.presence_of_element_located((By.ID, f"task-{pre_created_task.public_id}-details"))
    )
    tasks_list_url = live_server.url + reverse("task_list")

    actual_url = selenium_client.current_url
    expected_url = tasks_list_url

    assert actual_url == expected_url
