from .base import *

ALLOWED_HOSTS = ['3.34.233.43']




STATIC_ROOT = os.path.join(BASE_DIR,'static/')

STATICFILES_DIRS = []
# 오류방지



DEBUG = False

DATABASES ={
    'default':{
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME':'pybo',
        'USER':'dbmasteruser',
        'PASSWORD' : '<yI]G_m2Cz=oYk87}VKm3,7n6+oQV`%E',
        'HOST':'ls-22b2535b83fdd33a9c5b6a775ee5c64ad75af11e.cm03yddd5ogv.ap-northeast-2.rds.amazonaws.com',
        'PORT':'5432',
    }
}