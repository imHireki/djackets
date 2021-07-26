"""
Viewsets for product app's serializers

"""

# Django
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Django Rest Framework
from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status

# Product app
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductList(generics.ListAPIView):
    """
    Product List

    Return a Response with a `serialized queryset`
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[0:4]


class ProductDetail(generics.RetrieveAPIView):
    """
    Detail for a Product object

    Return Response with a `serialized object`
    """
    serializer_class = ProductSerializer

    def retrieve(self, request, category_slug, product_slug):
        obj = get_object_or_404(
            Product,
            category__slug=category_slug,
            slug=product_slug
        )
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(generics.RetrieveAPIView):
    """
    Detail for a Category object

    Return a Response with the `serialized obejct`
    """
    serializer_class = CategorySerializer

    def retrieve(self, request, category_slug):
        obj = get_object_or_404(Category, slug=category_slug)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


class Search(views.APIView):
    """
    Search funcion that receives a POST with a `query` string

    Return a Response with the `serialized queryset`
    """
    def post(self, *args, **kwargs):
        queryset, query = self.get_queryset()

        if not queryset or not query:
            raise exceptions.NotFound
        
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def get_queryset(self):
        query = self.request.data.get('query', '')

        queryset = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return queryset, query


class AddToCart(views.APIView):
    """
    Add to cart function that receives a GET with a `p_id` string

    Return a Response with the `serialized cart`
    """
    def get(self, *args, **kwargs): 
        p_id = self.request.GET.get('pid', '')
        if not p_id:
            raise exceptions.NotFound

        product = get_object_or_404(Product, id=p_id)

        cart = self.get_cart()

        self.add_to_cart(p_id, product, cart)

        self.request.session.save()
        return Response(cart, status.HTTP_201_CREATED)

    def get_cart(self):
        """ Get a cart or create one"""
        if not self.request.session.get('cart'):            
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']
        return cart

    def add_to_cart(self, p_id, product, cart):
        """ Add the product to the user's cart """
        name = product.name
        category = product.category.name
        description = product.description
        image = product.get_image()
        price = float(product.price)

        if not p_id in cart:
            cart[p_id] = {
                'name': name,
                'category': category,
                'description': description,
                'image': image,
                'price': price,
                'sum_items': price,
                'amount': 1,
            }
        else:
            cart[p_id]['amount'] += 1
            new_amount = cart[p_id]['amount']
            cart[p_id]['sum_items'] = price * new_amount
