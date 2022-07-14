from pyexpat.errors import messages
from unittest.util import _MAX_LENGTH
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app.models import CustomUser


# @login_required(login_url="/login")
def account_dashboard(request):
    return render(request, 'admin_templates/account.html')

def add_account(request):
    return render(request, 'admin_templates/add-account.html')

def add_clients(request):
    if request.method != "POST":
        HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get("username")
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        password = request.POST.get("password")
        address = request.POST.get("addres")
        email = request.POST.get("email")
        date_joined = request.POST.get("date-joined")
        try:
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, user_type=2,password=password, email=email,date_joined=date_joined)
            user.clients.address=address
            user.save()
            messages.success(request, 'Added Successfully')
            return HttpResponseRedirect('/add_clients')
        except:
            messages.error(request, 'Failed to add')
            return redirect('/add_clients')    

            