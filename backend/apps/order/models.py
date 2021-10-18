from django.contrib.auth.models import User
from django.db import models

from apps.product.models import Product


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='orders'
        )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
        )
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
        related_name='items'
        )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='items'
        )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
       return f'{self.id}'

