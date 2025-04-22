from typing import Any, Callable

from django.conf import settings
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse


class RateLimitMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response
        self.rate_limit = settings.RATE_LIMIT
        self.rate_limit_time = settings.RATE_LIMIT_TIME

    def __call__(self, request: HttpRequest) -> HttpResponse:
        client_ip = self.get_client_ip(request)
        key = f"ratelimit:{client_ip}"

        requests = cache.get(key, 0)

        if requests >= self.rate_limit:
            return HttpResponse(status=429)

        requests += 1

        cache.set(key, requests, timeout=self.rate_limit_time)

        response = self.get_response(request)

        return response

    def get_client_ip(self, request: HttpRequest) -> Any | None:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

        ip = x_forwarded_for.split(",")[0] if x_forwarded_for else request.META.get("REMOTE_ADDR")

        return ip
