from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255,label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255,label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ['email','first_name','last_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('Email is Taken!')
        return email
   
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password did not match!')
        return password2
    
    def save(self,commit = True):
        user = super(CustomUserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.active = False
        if commit:
            user.save()
        return user

class CustomUserUpdateForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = MyUser
        fields = ['email','password','first_name','last_name','is_active','is_staff']
    
    def clean_password(self):
        return self.initial['password']

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)


    
    

