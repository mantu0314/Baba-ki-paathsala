from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ manager to communicate with python cli using cutomize model """

    def create_user(self,email,name,phone,password,confirm_password,age,status):
        if not email:
            raise ValueError("user must have an email address")

        email=self.normalize_email(email)
        user=self.model(email=email,name=name,phone=phone,age=age,status=status)
        if password==confirm_password:
            user.set_password(password)
            user.save(using=self.db)
        else:
            print("password and confirm_password should be same")
        return user

    def create_superuser(self,email,name,phone,password,confirm_password,age,status):
        user=self.create_user(email,name,phone,password,confirm_password,age,status)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Customize model for database """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255,default='SOME STRING')
    phone=models.IntegerField(max_length=30,default=None)
    confirm_password=models.CharField(max_length=128)
    age=models.IntegerField(max_length=2,default=None)
    status=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','phone','confirm_password','age','status']

    def get_full_name(self):
        """ Function to get the full name """
        return self.name

    def get_short_name(self):
        """ Function to get the short name """
        return self.name

    def __str__(self):
        """ Function to get email """
        return self.email
