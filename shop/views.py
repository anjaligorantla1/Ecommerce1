from django.shortcuts import render

from shop.models import Products
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    c=Products.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!=''and item_name is not None:
        c=c.filter(title__icontains=item_name)   
    
    #paginator code

    paginator=Paginator(c,3)
    page=request.GET.get('page')
    c=paginator.get_page(page)
    return render(request,'shop/index.html',{'c':c})

def detail(request,id):
    c=Products.objects.get(id=id)
    return render (request,'shop/detail.html',{'c':c})