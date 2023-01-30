from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='pics')
    offer=models.BooleanField(default=False)


#for admin services adding
class Allservice(models.Model):
    servicename=models.CharField(max_length=100)

class justurke(models.Model):
    name=models.CharField(max_length=50)
    

#for booking storage
class Booking(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenum=models.CharField(max_length=15)
    cityname=models.CharField(max_length=100)
    serviced=models.CharField(max_length=100)
    datebook=models.DateField(auto_now=False,auto_now_add=False)
    statusbook=models.BooleanField(default=False)
    normalstatus=models.BooleanField(default=True)
    

