from django.contrib import admin, messages
from . import models
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse

# Register your models here.



class InventoryFilter(admin.SimpleListFilter):
        title = 'inventory'
        parameter_name = 'inventory'

        def lookups(self, request, model_admin):
                return [
                        ('<10' , 'Low')
                ]
        
        def queryset(self, request, queryset):
                if self.value() == '<10':
                        return queryset.filter(inventory__lt = 10)
                






@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
        # readonly_fields = ['title']
        # exclude = ['promotions']
        # fields = ['title' , 'slug']
       
        search_fields = ['title']
        autocomplete_fields = ['collection']
        prepopulated_fields = {
                'slug' : ['title']

        }
        actions = ['clear_inventory']
        # inlines = [TagInline]
        list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
        list_editable = ['unit_price']
        list_filter = ['collection', 'last_update', InventoryFilter]
        list_per_page = 10
        list_select_related = ['collection']



# ********ADDING CUSTOM COLUMN*****
        def collection_title(self, product):
                return product.collection.title

# ****** ADDING COMPUTED COLUMNS*****
        @admin.display(ordering='inventory')   # this decorator allows us to sort the computed column
        def inventory_status(self, product):
                if product.inventory < 10:
                        return 'Low'
                return 'OK'
        
# ******adding custom actions*******8
        @admin.action(description='Clear inventory')
        def clear_inventory(self, request, queryset):
                updated_count = queryset.update(inventory=0)
                self.message_user(
                        request,
                        f'{updated_count} products were successfully updated',
                        messages.SUCCESS
                )



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
        
        list_display = ['first_name', 'last_name', 'email', 'phone', 'birth_date', 'membership']
        list_editable = ['membership']
        ordering = ['first_name' , 'last_name']
        list_per_page = 10
        # search_fields =  ['first_name' , 'last_name']
        search_fields =  ['first_name__istartswith' , 'last_name__istartswith']



class OrderItemInline(admin.StackedInline):
        autocomplete_fields = ['product']
        min_num = 1
        max_num = 10
        model = models.OrderItem
        extra = 0



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = ['id', 'placed_at', 'customer']
        inlines = [OrderItemInline]
        autocomplete_fields = ['customer']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
        list_display = ['title', 'products_count']
        search_fields = ['title']

        @admin.display(ordering='products_count')
        def products_count(self, collection):
                
                # return collection.products_count
                url = (
                        reverse('admin:store_product_changelist')       #admin:app_model_page
                        + '?'
                        + urlencode({
                                'collection__id' : str(collection.id)
                        }))
                          
                # return format_html('<a href="http://google.com"> {} </a>', collection.products_count)
                return format_html('<a href="{}"> {} </a>', url, collection.products_count)
        


        def get_queryset(self, request):
                return super().get_queryset(request).annotate(
                        products_count = Count('product')
                )

# admin.site.register(models.Product, ProductAdmin)