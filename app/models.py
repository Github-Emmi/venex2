from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data = ((1, "User"), (2, "Client"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length= 30)

class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    btc_wallet = models.CharField(max_length=30, blank=True)
    Ethereum_wallet = models.CharField(max_length=30, blank=True)
    USDT_wallet = models.CharField(max_length=30, blank=True)
    Litecoin_wallet = models.CharField(max_length=30, blank=True)
    tron_wallet = models.CharField(max_length=30, blank=True)
    phone_no = models.CharField(max_length=25, blank=True)
    profile_pic = models.FileField() 
    gender = models.CharField(max_length= 225)
    address = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length= 225)
    profile_pic = models.FileField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    

class NotificationClients(models.Model):
    id = models.AutoField(primary_key=True)
    clients_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    notified = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(admin=instance)
        if instance.user_type==2:
            Clients.objects.create(admin=instance, address="", gender="")

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminuser.save()
    if instance.user_type==2:
        instance.clients.save()                     