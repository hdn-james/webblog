from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    roles = [
        ('Admin', 'Admin'),
        ('User', 'User')
    ]

    genders = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=genders, default='Male')
    birthday = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=10, choices=roles, default='User')


def get_expired_day():
    return timezone.now() + timezone.timedelta(days=30)


class AuthToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)
    created_day = models.DateTimeField(default=timezone.now)
    expired_day = models.DateTimeField(default=get_expired_day)

