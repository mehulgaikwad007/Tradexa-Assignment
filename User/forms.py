from django.forms import widgets
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate , get_user_model

from django import forms
from .models import User, Post

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),label='')
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Password'}),label='')
      

    def clean(self , *args , **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password :
            user = authenticate(email=email , password=password)

            if not user:
                raise forms.ValidationError('Authentication error')
            
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password ')

            if not user.is_active:
                raise forms.ValidationError('This user is not active')

            

        return super(LoginForm,self).clean(*args,**kwargs)




class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Password'}),label='')
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','username')
        labels = {
            'first_name' : '',
            'last_name' : '',
            'email' : '',
            'password' : '',
            'username' : '',
        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control ' , 'placeholder':'Enter First Name'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'password' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_qs = User.objects.filter(email=email)

            if email_qs.exists():
                raise forms.ValidationError("Email Address already being used")
            return email

