from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '167.172.109.147']
SECRET_KEY = 'django-insecure--jxsf@pi^*z=hvz8+=v3+f0-vqw+j^6)#^(*6$%jlfy#b&%u!6'

try:
    from .local import *
except ImportError:
    pass
