"""
Define the Django models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for the User model."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        self.save_user(user)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a superuser with the given email and password."""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        self.save_user(user)
        return user

    def save_user(self, user):
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    """User model with email, username and password."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
