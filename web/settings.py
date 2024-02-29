import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'YunBcidlcV93KX9RsUQIwegRv-djG-upZWbekmV6-Pa80g-OMLDzIYY00E6nPkL23FD9eEA05xapZ4QKVLU9lqCpwGHgpTEqFIDHyNkzPkFOUH3mYvBOq3Rxk6KytuUeJslgPAFyeFI8y5IPCg-5VryBxfiwGyilpSiv1P0mukVHvxEX20-mnnu62WaQsKfCJKEra89xPDfNcNDTnvMon144Sqf90YMwHvEEdjkbcgdW0G28Ysvxw8xTsc0WK3b4wZMQEMbnujD3QLKBfbQZdTLbpnqcuE-NiOe8ZNSCk1bHhO70PycH_rirNfdAsojotjZdV4Im1rBqrqWcqHjlfUsC27TxGkPqkTZEAG-lzUkdMJ65EgObaAFOC2CGx3wtLJM5wHSagSG_V9EeHgSu4qzZQyK5PHRSDaOiIG4fAfsXMMveInmuC8ma7zavPmMQsY-6Os48SauBartwvvw4ig63hRAKA5c-I73qoGfmXbJWyXF3SdiI'

DEBUG = True # local

ALLOWED_HOSTS = [
    
    'www.bloknot-ik.ru', 
    '.bloknot-ik.ru', 
    'localhost',
    '127.0.0.1',

] 
    
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'compressor',
    'tinymce',
    
    'user',
    'base',
    'app',
    'analytics',

    'blog',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]



ROOT_URLCONF = 'web.urls'

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            
            ],
        
        },
    
    },

]

WSGI_APPLICATION = 'web.wsgi.application'

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow' # local

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# scss

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

# email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True # local
#EMAIL_HOST_USER = 'kosyakovsn@gmail.com'
#EMAIL_HOST_PASSWORD = 'gigharagfknceknq' # local
#DEFkosyakovsn AULT_FROM_EMAIL = 'bloknotikk@gmail.com'


""" TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
} """