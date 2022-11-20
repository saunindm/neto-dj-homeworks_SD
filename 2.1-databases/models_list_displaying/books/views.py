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
        'books_page_list': page.object_list,
        'previous_pub_date': pub_dates_dict.get(f"{page_number - 1}"),
        'next_pub_date': pub_dates_dict.get(f"{page_number + 1}"),
        'page': page,
    }
    template = 'books/pagi.html'
    return render(request, template, context)
