DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    'pac',

    'tests.app.app_1.apps.App1Config',
    'tests.app.app_2',
]

ROOT_URLCONF = 'tests.app.urls'

SECRET_KEY = 'kick me'
