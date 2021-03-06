from os.path import dirname, join, abspath


def project_path(path):
    return abspath(join(dirname(__file__), path))


DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'south',

    'django_otp',
    'django_otp.plugins.otp_hotp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_email',

    'testproj.app',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            project_path('templates'),
        ]
    },
]

TEMPLATE_DIRS = [
    project_path('templates'),
]

SECRET_KEY = '9xZjgb6lM998dPRNQ3j7au86X5ZL17Jtme5N910Cp06u7j0QLWara6BH7N90clGQ'

ROOT_URLCONF = 'testproj.urls'

AUTH_USER_MODEL = 'app.TestUser'
