import stripe

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes
)

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


User = get_user_model()


@api_view(['post'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY

        paid_amount = sum(
            item.get('quantity') * item.get('product').price
            for item in serializer.validated_data['item']
        )

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Djackets.',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, paid_amount=paid_amount)
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        except Exception:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
    
    return Response(
        data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
    )


class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
        