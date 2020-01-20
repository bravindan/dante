from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    name =models.CharField(max_length=50)
    pic=models.ImageField(upload_to="pics")
    comment=models.TextField(max_length=200)
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
       return self.name

class user(models.Model):
     u_name=models.CharField(max_length=100,verbose_name="username")
     password=models.CharField(max_length=100)
     def __str__(self):
       return self.u_name    
