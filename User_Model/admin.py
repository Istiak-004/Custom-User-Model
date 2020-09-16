from django.contrib import admin
from django.contrib.auth.admin import Group

from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    form = CustomUserUpdateForm
    add_form = CustomUserCreationForm
    
    list_display =('email','first_name','last_name','is_staff','is_admin')
    list_filter = ('is_staff',)
    fieldsets = (
        ('Identity',{'fields':('email','password')}),
        ('Address',{'fields':('first_name','last_name')}),
        ('Activity',{'classes':('wide',),
        'fields':('is_active','is_staff','is_admin',)}),
    )
    add_fieldsets = (
        (
            'Register',
            {
                'classes': ('collapse',),
                'fields': (
                    'email', 'first_name', 'last_name', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MyUser,UserAdmin)
admin.site.unregister(Group)