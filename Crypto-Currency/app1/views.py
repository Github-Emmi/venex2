from turtle import setundobuffer
from django.shortcuts import render

# Create your views here.

def index(request):
     return render(request, 'jobs/index.html', {})

def about(request):
     return render(request, 'jobs/about.html', {})

def started(request):
     return render(request, 'jobs/started.html', {}) 

def faq(request):
     return render(request, 'jobs/faq.html', {})      

def affiliate(request):
     return render(request, 'jobs/affiliate.html', {})         

def contact(request):
     if request.method == "post":
          message_name = request.POST['name']
          message_email = request.POST['email']
          message_body = request.POST['message']
     else:     
          return render(request, 'jobs/contact.html', {})

def signup(request):
     return render(request, 'jobs/signup.html', {})

def login(request):
     return render(request, 'jobs/login.html', {})          