from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)

class Psc(models.Model):
     #title = models.ForeignKey(Category, on_delete=models.CASCADE)
     question= models.CharField(max_length=1000)
     apple=models.CharField(max_length=300)
     boy=models.CharField(max_length=300)
     cat=models.CharField(max_length=300)
     dog=models.CharField(max_length=300)
     answer=models.TextField(max_length=400)
     category = models.CharField(max_length=100)

class Home(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    link=models.CharField(max_length=200)     