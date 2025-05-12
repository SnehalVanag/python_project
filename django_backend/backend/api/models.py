from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('marketing', 'Marketing Team'),
        ('lead', 'Lead Generator'),
        ('franchise', 'Franchise Admin'),
        ('user', 'Customer')
    )
    role = models.CharField(max_length=20, choices=ROLES)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

class Franchise(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='products/')
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE)

class Lead(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class MarketingMaterial(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='marketing/')
    type = models.CharField(max_length=20)  # banner, pamphlet, etc
    created_at = models.DateTimeField(auto_now_add=True)