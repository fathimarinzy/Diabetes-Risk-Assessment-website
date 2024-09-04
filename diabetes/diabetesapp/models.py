from pickle import TRUE
from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100)
    contact=models.IntegerField()
    mail=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class feedback(models.Model):
    username=models.CharField(max_length=30)
    contact=models.IntegerField()
    mail=models.EmailField(max_length=30)
    message=models.TextField(max_length=300)

class Info(models.Model):
    Pregnancies=models.TextField(max_length=30)
    Glucose=models.TextField(max_length=30)
    Bloodpressure=models.TextField(max_length=30)
    Skinthickness=models.TextField(max_length=30)
    Insulin=models.TextField(max_length=30)
    BMI=models.TextField(max_length=30)
    Diabetespedigreefunction=models.TextField(max_length=30)
    Age=models.IntegerField()
    gender=models.CharField(max_length=30)

class doctor(models.Model):
    name=models.TextField(max_length=30)
    qualification=models.TextField(max_length=30)
    department=models.TextField(max_length=30)
    hname=models.TextField(max_length=30)
    experience=models.TextField(max_length=30)
    ctime=models.TextField(max_length=30)
    place=models.TextField(max_length=30)
    fee=models.IntegerField()
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

class appointments(models.Model):
    name = models.TextField(max_length=30)
    fee = models.IntegerField()
    username = models.TextField(max_length=30)
    contact = models.IntegerField()
    date = models.DateField(null=True)   
    hname = models.TextField(max_length=250)
    ctime = models.TextField(max_length=30)
    mail=models.EmailField(max_length=100)
    

  
    