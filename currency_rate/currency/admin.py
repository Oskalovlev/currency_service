from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "charcode",
        "date",
        "rate",
    )
    search_fields = ("charcode",)
    empty_value_display = "--пусто--"
