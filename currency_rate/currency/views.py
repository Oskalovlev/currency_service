from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Currency


@csrf_exempt
def rate_view(request):

    charcode = request.GET.get("charcode")
    date = request.GET.get("date")

    rate = Currency.objects.filter(charcode=charcode, date=date).first()

    try:
        return JsonResponse(
            {
                "charcode": rate.charcode,
                "date": rate.date.strftime("%Y-%m-%d"),
                "rate": rate.rate,
            }
        )
    except ValueError:
        print("Один из атрибудтов запроса не обработан.")
