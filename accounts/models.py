from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, phone, username, password=None, **extra_fields):

        if not phone:
            raise ValueError("Email not given...")
        user = self.model(phone=phone, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None, **etra_fields):

        user = self.create_user(phone=phone, username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, ):

    # User accounts information
    username = models.CharField(max_length=120)
    phone = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=120)
    town = models.CharField(max_length=120)

    # User status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'user_country', 'town']

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
