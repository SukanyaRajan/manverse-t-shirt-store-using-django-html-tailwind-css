from django.db import models

from users.models import User
from managers.models import Product


ORDER_STATUS_CHOICES = (

    ("pending" , "pending"),
    ("packed" , "packed"),
    ("shipped" , "shipped"),
    ("delivered" , "delivered"),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
    

    class Meta:
        db_table = 'customer_customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ["-id"]

    def __str__(self):
        return self.user.username
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=25)
    address = models.TextField()
    pincode = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    status = models.CharField(max_length=25, choices=ORDER_STATUS_CHOICES)
    is_paid = models.BooleanField(default=False)

 

    class Meta:
        db_table = 'manager_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ["-id"]

    def __str__(self):
        return self.product.name