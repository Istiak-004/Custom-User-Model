from django.contrib.auth.backends import  BaseBackend
from django.contrib.auth import get_user_model
from .models import *

class CustomBackEnds(BaseBackend):
    def authenticate(self,request,email = None,password = None,**kwargs):
        myuser = get_user_model()
        try:
            user = myuser.objects.get(email = email)
            if user.check_password('password'):
                return user
        except myuser.DoesNotExist:
            return None 
    def get_user(self,user_id):
        myuser = get_user_model()
        try:
            return myuser.objects.get(pk = user_id)             
        except myuser.DoesNotExist:
            return None
