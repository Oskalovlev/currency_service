from datetime import datetime

from django.db import models
from django.utils import timezone
from requests import get

from ..models import Currency


class CurrencyManager(models.Manager):

    def get_currency_data(self):

        response = get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        date_str = data["Date"]
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        date = date_obj.date()
        for currency in data["Valute"].values():
            if not Currency.objects.filter(
                charcode=currency["CharCode"]
            ).exists():
                Currency.objects.create(
                    charcode=currency["CharCode"],
                    date=date,
                    rate=currency["Value"],
                )
            else:
                Currency.objects.filter(charcode=currency["CharCode"]).update(
                    date=date,
                    rate=currency["Value"],
                )
