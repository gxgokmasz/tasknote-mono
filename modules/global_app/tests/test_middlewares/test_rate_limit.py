from django.urls import reverse


def test_rate_limit_middleware(client, settings):
    login_url = reverse("login")
    max_requests = 3
    settings.RATE_LIMIT = max_requests

    for _ in range(max_requests):
        client.get(login_url)

    response = client.get(login_url)

    actual_status_code = response.status_code
    expected_status_code = 429

    assert actual_status_code == expected_status_code
