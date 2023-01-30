from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination,Allservice,Booking

from django.contrib.auth.models import User,auth
from django.contrib import messages



#---------Homepage----------------------------------------------------------
def homepage(request):
    return render(request,'homepage.html')



#-------------REGISTER AVVATANIKI PAGE------------REGISTER HTML PAGE-------------
def register(request):
    return render(request,'register.html')



#REGISTER AVVATANIKI VERIFYING---------VERIFYING REGISTER DETAILS

def registerdetails(request):
    username=request.POST['name']
    email=request.POST['email']
    phno=request.POST['phno']
    password1=request.POST['password1']
    password2=request.POST['password2']

    status1=User.objects.filter(username=username).exists()
    status2=User.objects.filter(email=email).exists()
    s='!@#$%^&*()_+<>?/{[]}'
    s=set(s)
    passd=set(password1)
    new= s.intersection(passd)
    if len(new)==0:
        messages.error(request,'it must contain single symbol')
        return render(request,'register.html') 
    vas=list(filter(lambda x:x.isalpha(),password1))
    passd=sorted(vas)
    if passd[0].islower():
        messages.error(request,'it must contain single upperletter')
        return render(request,'register.html')
    if len(password1)<8:
        messages.error(request,'length has to be greater than 8')
        return render(request,'register.html')
    if password1==password2:

        if not status1:
            if not status2:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                messages.error(request,'Successfully Registered.')
                return render(request,'login.html')
            else:
                messages.error(request,'Email already existed')
                return render(request,'register.html')
        else:
            messages.error(request,'Username already existed')
            return render(request,'register.html')
    else:
        messages.error(request,'Enter valid password')
        return render(request,'register.html')


#----------LOG-IN AVVATANIKI PAGE-----------LOGIN PAGE HTML-----------

def login(request):
    return render(request,'login.html')



#---------------USER LOGIN DETAILS FROM HTML----------LOGGING DETAILS VERIFYING-----------
def logindetails(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        dest=Destination.objects.all()
        return render(request,'index.html',{'dests':dest})
    else:
        messages.error(request,'invalid credentials')
        return render(request,'login.html')



#--------USER LOGIN AYTHE OCHE PAGE------------------USER LOGGED-IN HOMEPAGE--------------------------------------
def index(request):
    if request.user.is_authenticated:
        dest=Destination.objects.all()
        return render(request,'index.html',{'dests':dest})
    return HttpResponse("<h1 align='center'>404 Found</h1>")



#-------------SEARCHING PLACES........................
def searching(request):
    if not request.user.is_authenticated:
        return HttpResponse(request,'<h1>404 Not Found</h1>')
    cityname=request.POST['cityname']
    found=Destination.objects.filter(name=cityname.capitalize())
    return render(request,'index.html',{'dests':found})


#.....................SERVICES................................
def serviceshowing(request):
    serv=Allservice.objects.all()
    return render(request,'services.html',{'services':serv})



#---------------------- Booking Page --------------BOOK CHESKUNE PAGE------------------------------
def BookingPage(request):
    if not request.user.is_authenticated:
        return HttpResponse(request,'<h1>404 Not Found</h1>')
    names=Allservice.objects.all()
    cities=Destination.objects.all()
    return render(request,'destinations.html',{'names':names,'cities':cities})



#BOOKING DETAILS IKKADIKI OSTHAY ----------ENTERING BOOKING DETAILS TO DB---------
def BookedDetails(request):
    if not request.user.is_authenticated:
        return HttpResponse(request,'<h1>404 Not Found</h1>')
    fullname=request.user.username
    phonenum=request.POST['number']
    email=request.user.email
    city=request.POST['city']
    serviced=request.POST['service']
    bookdate=request.POST['bookdate']
    got=list(Booking.objects.filter(cityname=city,datebook=bookdate))
    names=Allservice.objects.all()
    cities=Destination.objects.all()
    if len(got)>=5:
        statusbook=False
        messages.error(request,'Request Pending')
    else:
        statusbook=True
        messages.success(request,'Well Done ! Successfully Booked')
    store=Booking(fullname=fullname,email=email,phonenum=phonenum,cityname=city,serviced=serviced,datebook=bookdate,statusbook=statusbook)
    store.save()
    return render(request,'destinations.html',{'names':names,'cities':cities})



#------------------Success,pending,rejected status-----------------------------------
def BookStatus(request):
    name=request.user.email
    print(name)
    details=Booking.objects.filter(email=name)
    return render(request,'index1.html',{'details':details})

    

#LOGOUT AVVANIKI-----------------LOGOUT -----------------------------
def logout(request):
    if not request.user.is_authenticated:
        return HttpResponse(request,'<h1>404 Not Found</h1>')
    auth.logout(request)
    return render(request,'homepage.html')

#---------------------------------END---------------------------------------------
