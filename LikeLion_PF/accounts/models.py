from django.db import models

# Create your models here.

class Account (models.Model) :
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=10)
    userid=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class Meta :
    db_table="accounts"