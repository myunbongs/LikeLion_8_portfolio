from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account (models.Model) :
    userid=models.CharField(max_length=10,verbose_name='ID')
    email=models.CharField(max_length=100,verbose_name='email')
    username=models.CharField(max_length=10,verbose_name='username')
    password=models.CharField(max_length=10,verbose_name='password')
    
class Meta :
    db_table="accounts"