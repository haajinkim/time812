from django.db import models
from user.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    price = models.IntegerField()
    introduction_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)



class UserProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey("Product",on_delete=models.SET_NULL, null=True)
    buy_date = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateField(null=True)



