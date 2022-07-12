
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.

# class CustomUser(AbstractUser):
#     user_type_data = ((1, "HOD"), (2, "Clients"))
#     user_type = models.CharField(default=1, choices=user_type_data, max_length= 30)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 225)
    email = models.CharField(max_length= 225)
    password = models.CharField(max_length= 225)
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 225)
    email = models.CharField(max_length= 225)
    password = models.CharField(max_length= 225)
    # admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length= 225)
    profile_pic = models.FileField()
    address = models.CharField ( max_length= 225)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()    

class NotificationClients(models.Model):
    id = models.AutoField(primary_key=True)
    clients_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.user_type==1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type==2:
#             Clients.objects.create(admin=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.user_type==1:
#         instance.adminhod.save()
#     if instance.user_type==2:
#         instance.clients.save()                     