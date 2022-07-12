from django.shortcuts import render, redirect

def admin_dashboard(request):
    return render(request, 'admin_templates/main.html')