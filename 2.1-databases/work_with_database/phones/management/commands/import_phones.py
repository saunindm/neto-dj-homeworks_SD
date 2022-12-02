import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                phone_obj = Phone(
                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug='-'.join(phone['name'].lower().split(' ')),
                )
                phone_obj.save()
        pass


# В скрипте для переноса данных можно использовать метод create чтобы создавать и сохранять объект в один шаг.
# https://docs.djangoproject.com/en/4.0/ref/models/querysets/#create
