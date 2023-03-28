from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))

# bus_load=[row for row in reader]

def bus_stations(request):

    page_index=int(request.GET.get('page', 1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице


    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations_list=[]
        for row in reader:
            #print(row['Name'])
            item= {}
            item['Name']=row['Name']
            item['Street'] = row['Street']
            item['District'] = row['District']
            bus_stations_list.append(item)
    paginator=Paginator(bus_stations_list,10)
    page=paginator.get_page(page_index)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
