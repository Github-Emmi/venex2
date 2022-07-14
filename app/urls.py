from app import views, AdminView
from django.urls import path, re_path

urlpatterns = [
     ######                   #####
       ###  LANDING PAGE URL   ###
     ######                   #####
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('started', views.started, name='started'),
    path('faq', views.faq, name='faq'),
    path('affiliate', views.affiliate, name='affiliate'),
    path('contact', views.contact, name='contact'),
    path('sent/', views.sent, name='sent'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('signup/', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('do-login', views.do_login, name='do_login'),

    ##########################################
       ###    USER DASHBOARD PAGE URL ###
    ##########################################                  #####
    path('account-dashboard', AdminView.account_dashboard, name='account'),
    path('add-account', AdminView.add_account, name='add_account'),
    path('add_clients', AdminView.add_clients, name='add_clients'),
]