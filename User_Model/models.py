from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MYUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password = None):
        if not email:
            raise ValueError("Need a email adress")
        if not first_name:
            raise ValueError("Need a name")
        if not last_name:
            raise ValueError('Need a name')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,email,first_name,last_name,password):
        user = self.create_user(
            email = email,
            password=password,
            first_name = first_name,
            last_name = last_name
        )  
        user.is_active = True  
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True,verbose_name='Email Address')
    first_name = models.CharField(max_length=255,verbose_name='First Name')
    last_name = models.CharField(max_length=255,verbose_name='Last Name')
    date_joined = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = MYUserManager()

    def get_full_name(self):
        return '%s %s' % (self.first_name,self.last_name)
    def __str__(self):
        return self.email
    def has_perm(self,prem,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
