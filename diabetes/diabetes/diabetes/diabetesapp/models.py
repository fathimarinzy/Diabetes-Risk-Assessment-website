from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=100)
    contact=models.IntegerField()
    mail=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class feedback(models.Model):
    username=models.CharField(max_length=30)
    contact=models.IntegerField()
    mail=models.CharField(max_length=30)
    message=models.TextField(max_length=300)
    

