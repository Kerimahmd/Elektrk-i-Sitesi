from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render,get_list_or_404

from goods.models import Categories,Products
from goods.utils import q_search


def goods(request,category_slug="Hepsi"):

    page = request.GET.get('page',1)
    categories = Categories.objects.all()
    product = Products.objects.all() 
    query = request.GET.get('q',None)
    

    if query:
        product = q_search(query)

    elif category_slug == "Hepsi":
        product = Products.objects.all()
    
    else:
        product = get_list_or_404(Products.objects.filter(category_slug=category_slug))

    paginator = Paginator(product,3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Ürünler",
        'categories':categories,   
        'goods' :current_page,
        'slug_url': category_slug
}
    return render(request, 'goods/goods.html', context)


def product(request, product_slug, ):
    try:
        product = Products.objects.get(slug=product_slug)
    except Products.DoesNotExist:
        raise Http404("Ürün bulunamadı.")


    
    context = {
        'product': product,    
}
    return render(request, 'goods/product.html', context=context)







