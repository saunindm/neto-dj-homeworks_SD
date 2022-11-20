from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'min_price')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name').values()
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price').values()
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price').values()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
