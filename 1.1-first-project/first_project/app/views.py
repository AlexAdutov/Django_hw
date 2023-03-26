import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    #print(msg)
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории !!!!!!!

    path = os.getcwd()
    list_dir = os.listdir(path)

    #print("Files and directories in '", path, "' :")

    #print(msg)
    if not list_dir:
        raise NotImplemented
    #print(list_dir)
    return HttpResponse(list_dir)


def workdir_view2(request):
    template_name = 'app/dirs.html'
    path = os.getcwd()
    list_dir = os.listdir(path)
    context = {
        'list_dir': list_dir
    }
    return render(request, template_name, context)
