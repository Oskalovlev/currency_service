from django.db import models
from django.utils import timezone
from requests import get

from ..models import Currency


class CurrencyManager(models.Manager):

    def get_currency_data(self):
        response = get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        for currency in data["Valute"].values():
            Currency.objects.get_or_create(
                charcode=currency["CharCode"],
                date=timezone.now(),
                rate=currency["Value"],
            )
