from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import Q, F, Count, Min, Max, Avg, Value, Func, ExpressionWrapper, DecimalField, Sum
from django.db.models.functions import Concat
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem
from tags.models import TaggedItem


#   @transaction.atomic()
def say_hello(request):
    #   Exercise
    #   Customer with .com accounts
    #   queryset = Customer.objects.filter(email__icontains='.com')
    #   Collections that don't have a featured product
    #   queryset = Collection.objects.filter(featured_product__isnull=True)
    #   Products with low inventory
    #   queryset = Product.objects.filter(inventory__lt=10)
    #   Orders placed by customer where id=1
    #   queryset = Order.objects.filter(customer_id=1)
    #   Order items for products in collection 3
    #   queryset = OrderItem.objects.filter(product__collection_id=3)
    #   Products: inventory < 10 AND price < 20
    #   queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    #   Products: inventory < 10 OR price < 20
    #   queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    #   Sorting - Order By
    #   queryset = Product.objects.order_by('title')
    #   Sorting - Earliest
    #   queryset = Product.objects.earliest('title')
    #   Sorting - Latest
    #   queryset = Product.objects.latest('title')
    #   Limiting Results - Getting the first five elements
    #   queryset = Product.objects.all()[:5]
    #   Selecting field to Query
    #   queryset = Product.objects.values('id', 'title', 'collection__title')
    #   queryset = Product.objects.values_list('id', 'title', 'collection__title')
    #   Exercise - Select products that have been ordered and sort them by title
    #   queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    #   Select Related Objects
    #   We use select_related when we have 1 instance - e.g. product -> collection
    #   queryset = Product.objects.select_related('collection')
    #   We use prefetch_related when we have n instance - e.g. product -> promotions
    #   queryset = Product.objects.prefetch_related('promotions')
    #   We can combine also(it doesn't matter the order)
    #   queryset = Product.objects.prefetch_related('promotions').select_related('collection')
    #   Selecting related objects answer
    #   queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product')
    #   .order_by('-placed_at')[:5]
    #   Aggregate
    #   result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
    #   Aggregating Exercises
    #   How many orders do we have?
    #   result = Order.objects.filter(payment_status='F').aggregate(count=Count('id'))
    #   How many units of product 1 have we sold?
    #   result = OrderItem.objects.filter(product=1).aggregate(units_sold=Count('id'))
    #   How many orders has customer 1 placed?
    #   result = Order.objects.filter(customer=1).aggregate(count=Count('id'))
    #   What is the min, max and avg price of the products in collection 3?
    #   result = Product.objects.filter(collection=3).aggregate(min_price=Min('unit_price'),
    #   max_price=Max('unit_price'), avg_price=Avg('unit_price'))
    #   Annotating Objects
    #   queryset = Customer.objects.annotate(new_id=F('id') + 1)
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    # )
    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '),'last_name')
    # )
    #   Grouping Data
    #   How many orders for each customer?
    #   result = Customer.objects.annotate(Count('order'))
    #   Working with Expressions Wrapper
    #   discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    #   queryset = Product.objects.annotate(
    #     discounted_price=discounted_price
    #   )
    #   Exercises - Working with Expressions Wrapper
    #   Customers with their last order ID
    #   queryset = Customer.objects.annotate(last_order_id=Max('order__id'))
    #   Collections and count of their products
    #   queryset = Collection.objects.annotate(quantity_products=Count('product'))
    #   Customer with more than 5 orders
    #   queryset = Customer.objects.annotate(orders_count=Count('order')).filter(orders_count__gt=5)
    #   Customer and the total amount they've spent
    #   queryset = Customer.objects.annotate(
    #       amount_spent=Sum(F('order__orderitem__unit_price') * F('order__orderitem__quantity')))
    #   Top 5 best-selling products and their total sales
    #   queryset = Product.objects.annotate(
    #       total_sales=Sum(F('orderitem__unit_price') * F('orderitem__quantity'))).order_by('-total_sales')[:5]
    #   Querying Generic Relationships
    #   content_type = ContentType.objects.get_for_model(Product)
    #   queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #   )
    #   Custom Managers
    #   queryset = TaggedItem.objects.get_tags_for(Product, 1)
    #   Creating Objects
    #   collection = Collection()
    #   collection.title = 'Video Games'
    #   collection.featured_product = Product(pk=1)
    #   collection.save()
    #
    #   Updating objects
    #   Collection.objects.filter(pk=11).update(featured_product=None)
    #   Deleting Objects - Two Ways
    #   collection = Collection(pk=11)
    #   collection.delete()
    #   and
    #   Collection.objects.filter(id__gt=5).delete()
    #   Exercises - Creating, updating, deleting objects
    #   Create a shopping cart with an item
    #   shopping_cart = Cart()
    #   shopping_cart.save()
    #
    #   cart_item = CartItem()
    #   cart_item.cart = shopping_cart
    #   cart_item.product = Product(pk=1)
    #   cart_item.quantity = 1
    #   cart_item.save()
    #   Updating the quantity of an item
    #   CartItem.objects.filter(pk=1).update(quantity=2)
    #   Removing a cart
    #   cart = Cart(pk=1)
    #   cart.delete()
    #
    #   Transactions
    #   Wrap your transactions methods with @transaction.atomic in order to prevent
    #   any data loss/mistake or wrap into a with transaction.atomic(): block
    #
    #   with transaction.atomic():`
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()
    #
    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()
    #   Raw SQL Queries - Just use this when you hqve to deal with complex queries
    #   use cursor to use insert, delete, select queries
    #   Product.objects.raw('SELECT id, title FROM store_product')

    return render(request, 'hello.html', {'name': 'Raphael', 'result': []})
