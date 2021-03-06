from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--jxsf@pi^*z=hvz8+=v3+f0-vqw+j^6)#^(*6$%jlfy#b&%u!6'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['DJANGO_ALLOWED_HOSTS', '*', '127.0.0.1']

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
