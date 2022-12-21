from django.contrib import admin
from .models import Sensor, Measurement


# InLine-модели - спец. механизм, который позволяет встраивать в отображение текущей таблицы, отображение другой
# class SensorInline(admin.TabularInline):
#     model = Sensor  # модель, для которой будет выстраиваться inline
#     extra = 0  # дополнительный параметр дополнительные позиции, чтобы вручную не создавать
#

@admin.register(Sensor)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


@admin.register(Measurement)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature', 'created_at']
    # inlines = [SensorInline, ]
