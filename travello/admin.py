from django.contrib import admin
from .models import Destination,Booking
from .models import Allservice,justurke

# Register your models here.


#This is for adding cities
admin.site.register(Destination)

#This is for adding services
admin.site.register(Allservice)

admin.site.register(justurke)
#this is for booking 
admin.site.register(Booking)