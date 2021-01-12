from django.db import models
from user.models import User
# Create your models here.


class Thread(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_thread = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_day = models.DateTimeField(auto_now_add=True)
    hashtag = models.CharField(max_length=100, null=True)


class Content(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    types = [
        ('Picture', 'Picture'),
        ('Text', 'Text')
    ]
    value = models.CharField(max_length=1000, default='')
    type = models.CharField(max_length=10, choices=types)


class Emote(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    types = [
        ('Like', 'Like'),
        ('Unlike', 'Unlike')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=types)
    created_day = models.DateTimeField(auto_now_add=True)

