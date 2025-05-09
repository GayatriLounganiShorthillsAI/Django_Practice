from django.shortcuts import render
# from django.http import HttpResponse
from django.db.models import Q, F, Value, Func, ExpressionWrapper , DecimalField
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order, Customer, Collection
from django.db.models.aggregates import Count, Max, Min, Avg
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction, connection

# from rest_framework.generics import ListCreateAPIView

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
        # queryset = Product.objects.all()[5:10]
  

        # *****selecting fields to query******
        # queryset = Product.objects.values_list('id' , 'title', 'collection__title')

        # queryset = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')
        
        #*******Deferring fields******
        
        # queryset = Product.objects.only('id', 'title')
        # queryset = Product.objects.defer('description')

        # *****selecting related fields

        # select-related (1)
        # prefetch_related (n)
        # queryset = Product.objects.select_related('collection').all()
        # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

        # ***EXERCISE 

        # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
        # orders = Order.objects.prefetch_related('orderitem_set__product')
       

        # ******aggregate function*****
        # result = Product.objects.filter(collection__id = 5).aggregate(count = Count('id'), min_price = Min('unit_price'))

        # ***** annotating objects***
        # queryset = Customer.objects.annotate(new_id = F('id')+1)


        # *******calling database function****
        # queryset = Customer.objects.annotate(
        #         full_name = Func(F('first_name') , Value(' '), F('last_name'), function='CONCAT')
        # )
        # queryset = Customer.objects.annotate(
        #         full_name = Concat('first_name' ,Value(' ') , 'last_name')
        # )

        # ****grouping data***
        # queryset = Customer.objects.annotate(
        #         orders_count = Count('order')
        # )

        # *****working with expression wrappers***
        # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
        # queryset = Product.objects.annotate(
        #         discounted_price = discounted_price
        # )


        # ********querying generic relationships****
        # content_type = ContentType.objects.get_for_model(Product)
        # tag = TaggedItem.objects.filter(
        #       content_type=content_type,
        #       object_id=1
        # ).select_related('tag')
       
        # return render(request, 'hello.html', {'name' : 'Gayatri', 'tags' : list(tag)})


        # *********custom managers******
        
        # tag = TaggedItem.objects.get_tags_for(Product, 1)
        # return render(request, 'hello.html', {'name' : 'Gayatri', 'tags' : list(tag)})

        # *******understanding queryset cache*****
        # queryset = Product.objects.all()

        # # queryset[0] access element from cache
        # list(queryset)
        # queryset[0]

        # # there will be no cache

        # queryset[0]
        # list(queryset)
        

        # ******creating objects*******
        # collection = Collection()
        # collection.title = 'Video_games'
        # collection.featured_product = Product(pk = 1)
        # # collection.featured_product_id = 1
        # collection.save()

        # or modern approach but "title" won't change if its name is changed in making models
        # collection = Collection.objects.create(title='a' , featured_product_id=1)


        # *******updating objects******
        # collection = Collection(pk = 1)
        # collection.title = 'hello'
        # collection.featured_product = None
        # # collection.featured_product_id = 1
        # collection.save()


        # collection = Collection.objects.filter(pk=1).update(featured_product = None)


        # ******deleting objects*****
        # collection = Collection(pk = 1)
        # collection.delete()

        # collection = Collection.objects.filter(pk= 1).delete()

        # *****transactions*******
        # with transaction.atomic():
        #         order = Order()
        #         order.customer_id = 1
        #         order.save()

        #         item = OrderItem()
        #         item.order = order
        #         item.product_id = 1
        #         item.quantity = 1
        #         item.unit_price = 10
        #         item.save()


        # ********executing raw sql queries******

        # queryset = Product.objects.raw('SELECT * FROM store_product')

        # OR

        with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM store_product')
                # cursor.callproc('get_customers', [1,2,'a'])


        return render(request, 'hello.html', {'name' : 'Gayatri', 'tags' : (cursor)})
