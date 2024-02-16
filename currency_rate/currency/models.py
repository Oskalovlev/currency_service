from django.db import models


class Currency(models.Model):
    """Денежная единица."""

    charcode = models.CharField(
        "Код валюты",
        max_length=3,
    )
    date = models.DateField(
        "Дата",
    )
    rate = models.FloatField(
        "Ставка к рублю",
    )

    def __str__(self):
        return f"{self.charcode} на {self.date} = {self.rate}"

    class Meta:
        verbose_name = "Денежная единица"
