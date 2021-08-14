from django.contrib.auth import get_user_model
from django.db import models 

from apps.product.models import Product


User = get_user_model()
CASCADE = models.CASCADE


class Order(models.Model):
    user = models.ForeignKey(
        to=User, related_name='orders', on_delete=CASCADE
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.first_name
    

class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, related_name='items', on_delete=CASCADE
    )
    product = models.ForeignKey(
        to=Product, related_name='items',  on_delete=CASCADE
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)
