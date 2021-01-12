import random
import string
from django.utils import timezone

from user.models import User, AuthToken
from post.models import Thread
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password

from post.controllers import get_thread_detail


def get_user_by_token(token: str):
    try:
        auth_token = AuthToken.objects.get(token=token, expired_day__gt=timezone.now())
        return auth_token.user
    except AuthToken.DoesNotExist:
        return None


def get_random_string(length: int):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def sign_in(username: str, password: str):
    password = make_password(password, 'ok', "pbkdf2_sha256")
    try:
        user = User.objects.get(username=username, password=password)
        while True:
            token = get_random_string(50)
            try:
                auth_token = AuthToken.objects.get(token=token)
            except Exception:
                auth_token = AuthToken(user=user, token=token)
                auth_token.save()
                return token
    except User.DoesNotExist:
        return None


def sign_up(username: str, password: str):
    password = make_password(password, 'ok', "pbkdf2_sha256")
    user = User(username=username, password=password)
    try:
        user.save()
        return True
    except IntegrityError:
        return None


def sign_out(auth_token: str):
    AuthToken.objects.filter(token=auth_token).delete()


def get_user_detail(user: User):
    threads = Thread.objects.filter(author=user, parent_thread__isnull=True)
    hashtags = [thread.hashtag for thread in threads]
    return {
        'username': user.username,
        'hashtags': hashtags,
        'threads': [
            get_thread_detail(thread) for thread in threads
        ]
    }



