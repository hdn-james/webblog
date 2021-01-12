from cs300_webblog.settings import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_blog',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    }
}