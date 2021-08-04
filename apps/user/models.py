"""
Include Custom model`User`
for the creation of Users and Superusers
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from . import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """ Creates and saves a user with the given email and password """
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        """ Creates and saves a superuser with the given email and password """
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """ Custom User model with the `email` as the `USERNAME_FIELD`"""
    email = models.EmailField(max_length=255, unique=True)
    username = None # Excluded field
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
