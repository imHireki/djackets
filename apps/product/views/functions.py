"""
Views to be used as functions
"""

# Django
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Django Rest Framework
from rest_framework.response import Response
from rest_framework import exceptions, status, views

# Product app
from ..models import Product
from ..serializers import ProductSerializer


class SearchProducts(views.APIView):
    """
    Search funcion that receives a GET with a `query` string

    Return a Response with the `serialized queryset`
    """
    def get(self, *args, **kwargs):
        queryset, query = self.get_queryset()
        if not queryset or not query:
            raise exceptions.NotFound
        
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        query = self.request.GET.get('query', '')

        queryset = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return queryset, query


class AddToCart(views.APIView):
    """
    Add to cart function that receives a POST with a `pid` string

    Return a Response with the `serialized cart`
    """
    def post(self, *args, **kwargs): 
        pid = self.request.data.get('pid', '')
        if not pid: raise exceptions.NotFound

        product = get_object_or_404(Product, id=pid)
        cart = self.get_or_create_cart()
        self.add_to_cart(pid, product, cart)

        self.request.session.save()
        return Response(cart, status.HTTP_201_CREATED)

    def get_or_create_cart(self):
        """ Get a cart or create one"""
        if not self.request.session.get('cart'):            
            self.request.session['cart'] = {}
            self.request.session.save()

        return self.request.session['cart']

    def add_to_cart(self, pid, product, cart):
        """ Add the product to the user session's cart """
        name = product.name
        category = product.category.name
        description = product.description
        image = product.get_image()
        price = float(product.price)

        if not pid in cart:
            cart[pid] = {
                'name': name,
                'category': category,
                'description': description,
                'image': image,
                'price': price,
                'sum_items': price,
                'amount': 1,
            }
        else:
            cart[pid]['amount'] += 1
            new_amount = cart[pid]['amount']
            cart[pid]['sum_items'] = price * new_amount


class DecreaseOrDeleteFromCart(views.APIView):
    """
    Decrease from cart function that receives a PATCH with the `pid`

    Return a Response with the `serialized cart`
    """
    def patch(self, *args, **kwargs):
        pid = self.request.data.get('pid')
        if not pid: raise exceptions.ParseError

        cart = self.get_cart()
        if not cart: raise exceptions.ParseError

        if not pid in cart: raise exceptions.NotFound

        product = get_object_or_404(Product, id=pid)

        self.remove_from_cart(cart, pid)
        return Response(cart, status=status.HTTP_200_OK)

    def get_cart(self):
        """ Get cart """
        return self.request.session.get('cart', {})

    def remove_from_cart(self, cart, pid):
        """ Remove `pid` from `cart` or adjust `amount` and `sum_items` """
        if cart[pid]['amount'] == 1:  del cart[pid]
        else:
            cart[pid]['amount'] -= 1

            price = cart[pid]['price']
            cart[pid]['sum_items'] = price * cart[pid]['amount']

        self.request.session.save()


class DeleteFromCart(DecreaseOrDeleteFromCart, views.APIView):
    """
    Delete a product function that receives a DELETE with the `pid`

    Return a Response with the `serialized cart`
    """
    def delete(self, request, *args, **kwargs):
        pid = self.request.data.get('pid')
        if not pid: raise exceptions.NotFound

        cart = self.get_cart()
        if not cart: raise exceptions.NotFound
        if not pid in cart: raise exceptions.NotFound

        del cart[pid]
        self.request.session.save()
        return Response(cart, status=status.HTTP_200_OK)
