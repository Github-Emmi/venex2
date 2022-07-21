from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from app.models import CustomUser

def account_dashboard(request):
    return render(request, 'admin_templates/account.html')


def add_clients(request):
    return render(request, 'admin_templates/add-clients.html')

def save_clients(request):
    if request.method!= "POST":
        return HttpResponse("</h2>Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,user_type=2)
            user.staffs.address=address 
            user.save()
            
            messages.success(request, 'Successfully Added Staff.')
            return HttpResponseRedirect('/add-clients')
        except:
            messages.error(request, 'failed To Add Staff.')
            return HttpResponseRedirect('/add-clients')

            