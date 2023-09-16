from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']


class UserAddress(models.Model):
    _id = models.IntegerField(blank=True, null=True,editable=False)
    alias = models.CharField(max_length=100)
    details = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    postalCode = models.CharField(max_length=10, null=True, blank=True)

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='addresses')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.id != self._id:
            self._id = self.id
            self.save()

    def __str__(self):
        return str('(' + self.user.username + ') ' + self.alias)
