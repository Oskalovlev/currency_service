from django.urls import path

from .views import rate_view

app_name = "currency"

urlpatterns = [
    path("", rate_view, name="rate"),
]
