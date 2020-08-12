from .base import *
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5i4romsilvak9',
        'USER': 'pdmnomwcconlrz',
        'PASSWORD': '43cb9cb2f4ecca9ebde1b244972ad08c76f935fda5a849cfcaaf0f7a8ca9cefc',
        'HOST': 'ec2-35-175-155-248.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')