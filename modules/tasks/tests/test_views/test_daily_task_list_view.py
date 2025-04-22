from datetime import datetime

import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ...src.infrastructure.models import Task


@pytest.mark.parametrize("selenium_client", [{"authenticated": True}], indirect=True)
@pytest.mark.django_db(transaction=True)
def test_daily_tasks_loaded(live_server, create_task, selenium_client) -> None:
    task = Task.objects.get(title="Task 0")
    task.finish_date = datetime.today().date()
    task.save()
    daily_tasks_list_url = live_server.url + reverse("task_daily")
    selenium_client.get(daily_tasks_list_url)
    created_task_card_exists = (
        WebDriverWait(selenium_client, 10)
        .until(EC.presence_of_element_located((By.ID, f"task-{task.public_id}-details")))
        .is_displayed()
    )

    actual_task_card_existence = created_task_card_exists
    expected_task_card_existence = True

    assert actual_task_card_existence == expected_task_card_existence
