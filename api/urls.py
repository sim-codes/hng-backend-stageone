from django.urls import path

from .views import CityTemperatureView

urlpatterns = [
    path('hello/', CityTemperatureView.as_view(), name='hello-world'),
]