from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.

###########################################################
     #Landing Page views
###########################################################

def index(request):
    return render(request, 'jobs/index.html', {})

def about(request):
     return render(request, 'about.html', {})

def started(request):
     return render(request, 'started.html', {}) 

def faq(request):
     return render(request, 'faq.html', {})

def affiliate(request):
     return render(request, 'affiliate.html', {})

def terms(request):
     return render(request, 'terms.html', {})              

def contact(request):
     return render(request, 'jobs/contact.html', {})   

def sent(request):
     if request.method == "POST":
          message_name = request.POST['name']
          message_email = request.POST['email']
          message = request.POST['message']
          # send an email 
          send_mail(
               'New message from ' + message_name, 
               message,
               message_email,
               ['venexltd@gmail.com', 'aghason.emmanuel@gmail.com'],
          )
          return render(request, 'jobs/sent.html', {
               'message_name': message_name,
               ' message_email': message_email,
               'message' : message,
               })
     else:
          return render(request,'jobs/index.html')  

def signup(request):
     return render(request, 'jobs/signup.html', {})              

def login(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user!= None:
              login(request,user)
              return render(request, 'about.html')
         else:
              messages.error(request, "Please enter the correct email and password")
              return render(request, 'login.html')
    return render(request, 'login.html')         


def get_details(request):
    if request.user!= None:
        return HttpResponse("Emial: "+request.user.email + " user_type: "+request.user.user_type)
    else:
        HttpResponse("login first")    

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

