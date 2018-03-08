import os

DATABASES = {}

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('PG_DATABASE_NAME', ''),
    'USER': os.getenv('PG_DATABASE_USER', ''),
    'PASSWORD': os.getenv('PG_DATABASE_PASSWORD', ''),
    'PORT': '5432',
}