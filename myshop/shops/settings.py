import django
django.setup()

from models import shops


INSTALLED_APPS = [
    # Other apps
    'rest_framework',
    'shops',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shopdb',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
