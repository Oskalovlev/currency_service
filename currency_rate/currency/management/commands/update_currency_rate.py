from django.core.management.base import BaseCommand

from ..currensy_manager import CurrencyManager


class Command(BaseCommand):

    help = "Обновляет данные о курсах валют раз в сутки."

    def handle(self, *args, **options):
        CurrencyManager().get_currency_data()
        self.stdout.write(
            self.style.SUCCESS("Данные о курсах валют успешно обновлены.")
        )
