from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import register_converter

from books.models import Book


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)

register_converter(DateConverter, 'date')

def books_view(request):
    books = Book.objects.all().order_by('name')
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def books_list(request, pub_date):
    books = Book.objects.all().order_by('pub_date')
    date_list = [book.pub_date.isoformat() for book in books]
    print(date_list)
    paginator = Paginator(books, 1)
    page = paginator.get_page(date_list.index(pub_date.date().isoformat()) + 1)
    template = 'books/books_list_pagi.html'
    context = {'page': page,
               }
    return render(request, template, context)