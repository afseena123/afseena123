from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from shopping.models import *


# Create your models here.
class cartlist(models.Model):
    cartid=models.CharField(max_length=100,unique=True)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.cartid

class cartitem(models.Model):
 
    active=models.BooleanField(default=True)
    quantity=models.IntegerField()
    
    product=models.ForeignKey(prducts,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product)
    


    



class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist,on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    towncity = models.CharField(max_length=20)
    postcodezip = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()



class payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    expiry_month=models.CharField(max_length=2)
    cvv=models.CharField(max_length=3)






