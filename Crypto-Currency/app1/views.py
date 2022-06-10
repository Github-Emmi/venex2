from django.shortcuts import render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template import loader
from django import template
from .models import profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList


# Create your views here.

###########################################################
     #Landing Page views
###########################################################
def index(request):
     return render(request, 'index.html', {})

def about(request):
     return render(request, 'about.html', {})

def started(request):
     return render(request, 'started.html', {}) 

def faq(request):
     return render(request, 'faq.html', {})      

def affiliate(request):
     return render(request, 'affiliate.html', {})         

def contact(request):
     return render(request, 'contact.html', {})

def signup(request):
     msg     = None
     success = False
     
     if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            profile.objects.create(user=user)
            

            msg     = 'User created - please login.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
     else:
        form = SignUpForm()
     return render(request, 'signup.html', {"form": form, "msg" : msg, "success" : success })



def login(request):
     form = LoginForm(request.POST or None)
     msg = None

     if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    
     return render(request, 'login.html', {"form": form, "msg" : msg})          


##################################################################

          #Dashboard Views

##################################################################



# @login_required(login_url="/login/")
def dashboard(request):
    return render(request, "main.html")


# @login_required(login_url="/login/")
def depositHistory(request):
    return render(request, "deposit.html")



# @login_required(login_url="/login/")
def earnings(request):
    return render(request, "earnings.html")



# @login_required(login_url="/login/")
def investments(request):
    return render(request, "my-investments.html")




# @login_required(login_url="/login/")
def purchasePlan(request):
    return render(request, "purchase-plan.html")










####################################################################

          #Error page Catcher

####################################################################

# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
