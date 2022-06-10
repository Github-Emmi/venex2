
from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import profile 
# Withdraw, fund, userwallet

from django.contrib.auth.forms import UserCreationForm
from .models import profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')







class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



class profileEditForm(forms.ModelForm): 
    
    class Meta:
        model = profile
        fields = ['btc_address', 'eth_address', 'usdt_address']

    




   
class creditEditForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['fund_amount', 'fund_method']





class DebitEditForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['withdrawal_amount', 'withdrawal_method']