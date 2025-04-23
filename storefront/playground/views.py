from django.shortcuts import render
# from django.http import HttpResponse
from django.db.models import Q, F
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
        # queryset = Product.objects.filter(Q(inventory__lt = 10) & ~Q(unit_price__lt = 20))
        # queryset = Product.objects.filter(inventory = F('collection__id') )


        # *******sorting*******
        # queryset = Product.objects.order_by('unit_price','-title').reverse()
        # product = Product.objects.order_by('unit_price')[0]    # order by return the query set 
        # product = Product.objects.earliest('unit_price')   #returns the top element
        # product = Product.objects.latest('unit_price')   #sort in desecending order and return the last element
   

        # ********limiting result***********
        # 0,1,2,3,4 excluding top 5
        queryset = Product.objects.all()[5:10]
  

        # *****selecting fields to query******

        return render(request, 'hello.html', {'name' : 'Gayatri', 'products' : list(queryset)})
 