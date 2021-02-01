from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Copoun(models.Model):
    company = models.ForeignKey(Company, related_name='coupons', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    assigned_users = models.ManyToManyField(CustomUser, related_name='assigned_copouns', through='CopounAssignment')

class CouponAssignment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Copoun, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)
