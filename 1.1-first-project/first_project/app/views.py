from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    base_path = os.getcwd()
    files_list = os.listdir(base_path)
    msg = f'Список файлов в рабочей директории: {files_list}'
    return HttpResponse(msg)

# Здравствуйте, Дмитрий! Вы успешно справились с первым заданием по курсу Django!
# Добавлю лишь один небольшой совет если вы не против) Используйте функцию strftime модуля datetime чтобы отформатировать отображение времени на странице
# https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/
