from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    stations_list = list(reader)


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    page_stations_list = stations_list[(page_number - 1) * 10: page_number * 10]
    print(page.has_next())
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)

# Такого рода вычисления
# page_stations_list = stations_list[(page_number - 1) * 10: page_number * 10]
# нам ни к чему. Информация о списке станций на текущей странице хранится в page.object_list
# Зачтено. Хорошего понедельника!
