from webblog.settings import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_blog',
        'HOST': 'db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'PORT': 5432,
    }
}

DEBUG = True
