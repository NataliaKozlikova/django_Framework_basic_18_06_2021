from django.shortcuts import render


def index(request):
    title = 'магазин'
    context = {
        'title': title
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title
    }
    return render(request, 'geekshop/contact.html', context=context)
