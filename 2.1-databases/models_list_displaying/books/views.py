from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def books_list(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def book(request, pub_date):
    books = Book.objects.all().order_by('pub_date').values()
    pub_dates = [x['pub_date'] for x in books]
    pub_dates_upd = [x.strftime('%Y-%m-%d') for x in pub_dates]  # список дат публикаций
    page_number = pub_dates_upd.index(pub_date) + 1
    pub_dates_dict = {}
    for i, date in enumerate(pub_dates_upd):
        pub_dates_dict[f"{i + 1}"] = date  # словарь с датами публикаций и соответствующими им номерами страниц
    books = Book.objects.all().order_by('pub_date')
    paginator = Paginator(books, 1)
    page = paginator.get_page(page_number)
    context = {
        'books': page.object_list,
        'previous_pub_date': pub_dates_dict.get(f"{page_number - 1}"),
        'next_pub_date': pub_dates_dict.get(f"{page_number + 1}"),
        'page': page,
    }
    template = 'books/pagi.html'
    return render(request, template, context)


# Касаемо второго дополнительного задания. В этом задании не нужно использовать встроенный Django-пагинатор. У него несколько иной функционал который под это
# задание не подходит. Есть более простой вариант. Отправляя url-запрос с конкретной датой вы получаете эту дату как обычную переменную. Книги нужно отфильтровать
# по дате получив тем самым книгу с заданной датой, а так же следующей и предыдущей. Посмотрите в документации про фильтры “больше”, "меньше"
# https://docs.djangoproject.com/en/4.0/topics/db/queries/#filters-can-reference-fields-on-the-model
# Пример
# def books_pub_date(request, pub_date):
#     template = 'books/books_list.html'
#     books_objects = Book.objects.filter(pub_date=pub_date)
#     books_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
#     books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
#     context = {
#         'books': books_objects,
#         'next_book': books_next,
#         'previous_book': books_previous,
#     }
#     return render(request, template, context)
