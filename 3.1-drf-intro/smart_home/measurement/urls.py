from django.urls import path
from django.contrib import admin

from measurement.views import UpdateViewSensor, CreateMeasurement, CreateSensor

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensor.as_view()),
    path('sensors/<pk>/', UpdateViewSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
