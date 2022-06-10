from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.fields import CharField



# Create your models here.

amount = (
    ('none', 'Select Amount'),
    ('200', '200'),
    ('500', '500'),
    ('1000', '1,000'),
    ('5000', '5,000'),
    ('10000', '10,000'),
)

method = (
    ('none', 'Select Method'),
    ('BTC', 'Bitcoin'),
    ('ETH', 'Ethereum'),
    ('USDT', 'USDT(Tether)'),
)


class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fund_method = models.CharField(max_length=7, choices=method, default='none')
    fund_amount = models.CharField(max_length=15, choices=amount, default='none')
    withdrawal_amount = models.CharField(max_length=15, null=True)
    withdrawal_method = models.CharField(max_length=15, choices=method, default='none')
    btc_address = models.CharField(max_length=500, blank=True, null=True)
    eth_address = models.CharField(max_length=500, blank=True, null=True)
    usdt_address = models.CharField(max_length=500, blank=True, null=True)
    


    def __str__(self):
        return f'Profile for user {self.user.username}'

