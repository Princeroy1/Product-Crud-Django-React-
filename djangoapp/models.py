from django.db import models

# Create your models here.
class Products(models.Model):
    img=models.ImageField(upload_to='myimg')
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=5,max_length=50,decimal_places = 2)
    discription=models.CharField(max_length=1000)
    stock=models.IntegerField()