from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from app.models import CustomUser

def account_dashboard(request):
    return render(request, 'admin_templates/account.html')

<<<<<<< HEAD

=======
>>>>>>> 8a523609b7bb04b3c2d4726d97d6a63c748462d3
def add_clients(request):
    return render(request, 'admin_templates/add-clients.html')

def save_clients(request):
<<<<<<< HEAD
    if request.method!= "POST":
        return HttpResponse("</h2>Method Not Allowed")
=======
    if request.method != "POST":
        HttpResponse("<h2>Method Not Allowed</h2>")
>>>>>>> 8a523609b7bb04b3c2d4726d97d6a63c748462d3
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
<<<<<<< HEAD
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,user_type=2)
            user.staffs.address=address 
            user.save()
            
=======
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password,user_type=2)
            user.clients.gender=sex
            user.save()            
>>>>>>> 8a523609b7bb04b3c2d4726d97d6a63c748462d3
            messages.success(request, 'Successfully Added Staff.')
            return HttpResponseRedirect('/add-clients')
        except:
            messages.error(request, 'failed To Add Staff.')
            return HttpResponseRedirect('/add-clients')

            