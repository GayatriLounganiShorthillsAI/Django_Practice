from django.shortcuts import render
# from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

# Create your views here.
# req -> Response
# request handler
# action

def calculate():
        x = 1
        y = 2
        return x

def say_hello(request):
        # return HttpResponse('Hello world')
        # x = calculate()

        # try:
        #    product = Product.objects.get(pk = 0)

        # except ObjectDoesNotExist :
        #    pass
        
        # None
        # product = Product.objects.filter(pk = 0).exists()

        # *********filtering*******

        # queryset = Product.objects.filter(unit_price__range = (20, 30))
        # queryset = Product.objects.filter(inventory__lt = 10).filter(unit_price__lt = 20)
        queryset = Product.objects.filter(Q(inventory__lt = 10) & ~Q(unit_price__lt = 20))

        return render(request, 'hello.html', {'name' : 'Gayatri', 'products' : list(queryset)})
 