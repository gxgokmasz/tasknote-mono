from datetime import date

from django.utils import timezone


class DateProcessingMixin:
    def get_today(self) -> date:
        return timezone.now().date().today()

    def get_outdated_dates(self, dates: list[date], today: date) -> list[date]:
        return [date for date in dates if date is not None and date < today]
