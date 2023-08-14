
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class CustomManager(BaseUserManager):
    def create_user(self,email,fName,lName,password=None):
        if not email:
            raise ValueError('Enter a valid Email address')
        NE=self.normalize_email(email)
        CUO=self.model(email=NE,fName=fName,lName=lName)
        CUO.set_password(password)
        CUO.save()
        return CUO
    def create_superuser(self,email,fName,lName,password):
        CUO=self.create_user(email,fName,lName,password)
        CUO.is_staff=True
        CUO.is_superuser=True
        CUO.save()

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    fName=models.CharField(max_length=100)
    lName=models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    # connecting CustomUser to CustomManager to do operations using BaseUserMamnager methods
    objects=CustomManager()
    # Used to make it as authentication fields
    USERNAME_FIELD='email'
    # Used to make it as Mandatory fields
    REQUIRED_FIELDS=['fName','lName']

    def __str__(self):
        return self.fName
