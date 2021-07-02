from django.shortcuts import render

from mainapp.models import ProductCategory


def products(request):
    title = 'продукты/каталог'
    categories = ProductCategory.objects.all()

    context = {
        'title': title,
        'categories': categories,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)