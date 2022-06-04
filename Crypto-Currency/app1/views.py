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
     return render(request, 'jobs/contact.html', {})

def signup(request):
     return render(request, 'jobs/signup.html', {})

def login(request):
     return render(request, 'jobs/login.html', {})          