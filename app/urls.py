from app import AdminView
from . import views
from django.urls import path, re_path

urlpatterns = [
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
    path('logout', views.logout, name='logout'),
    path('get-user-detail', views.get_details, name='user_details'),

    ### admin urls
    path('admin-home', AdminView.admin_dashboard),
]