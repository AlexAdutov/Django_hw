from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    sort_field = request.GET.get('sort')
    if sort_field == 'name':
        phones = Phone.objects.all().order_by(sort_field)
    elif sort_field == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sort_field == 'min_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones, }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug)
    template = 'product.html'
    context = {'phone': phone[0]}
    return render(request, template, context)