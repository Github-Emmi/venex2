from venex_app import views, AdminView
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
    path('terms-and-conditions', views.terms, name='terms'),
    path('signup/', views.signup, name='signup'),
    path('login', views.user_login, name='login'),
    path('do-login', views.DoLogin, name='do_login'),

    ##########################################
       ###    USER DASHBOARD PAGE URL ###
    ##########################################  
    path('account-dashboard', AdminView.account_dashboard, name='account'),
    path('deposit-list', AdminView.deposit_list, name='deposite_list'),
    path('earning-history', AdminView.earning_history, name='earning_history'),
    path('security', AdminView.security, name='security'),
    path('edit-account', AdminView.edit_account, name='edit_account'),
    # path('edit-account-save', AdminView.deposit_list, name='edit_account_save'),
    # path('deposit', AdminView.deposit_list, name='deposite'),
    # path('withdraw', AdminView.deposit_list, name='withdraw'),
    path('add-clients', AdminView.add_clients, name='add_clients'),
    path('save-clients', AdminView.save_clients, name='save_clients'),
]