"""
Django settings for heqian project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bg6m3hba+lx^d$e%78rw)$5vbeuk#e*w7npd7e%$^7wdi6x)1f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.52ky.net', '39.107.226.248', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jinja',
    'olreg',
    'user',
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

ROOT_URLCONF = 'heqian.urls'


TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # Match the template names ending in .html but not the ones in the admin folder.
            'match_extension': '.html',
            'match_regex': r'^(?!admin/).*',
            'app_dirname': 'templates',

            # Can be set to 'jinja2.Undefined' or any other subclass.
            'undefined': None,

            'newstyle_gettext': True,
            # 'tests': {
            #     'mytest': 'path.to.my.test',
            # },
            # 'filters': {
            #     'myfilter': 'path.to.my.filter',
            # },
            'globals': {
                'reverse': 'django.core.urlresolvers.reverse',
                'auth_url': 'utils.tool.auth_url',
            },
            # 'constants': {
            #     'foo': 'bar',
            # },
            'extensions': [
                'jinja2.ext.do',
                'jinja2.ext.loopcontrols',
                'jinja2.ext.with_',
                'jinja2.ext.i18n',
                'jinja2.ext.autoescape',
                'django_jinja.builtins.extensions.CsrfExtension',
                'django_jinja.builtins.extensions.CacheExtension',
                'django_jinja.builtins.extensions.TimezoneExtension',
                'django_jinja.builtins.extensions.UrlsExtension',
                'django_jinja.builtins.extensions.StaticFilesExtension',
                'django_jinja.builtins.extensions.DjangoFiltersExtension',
            ],
            'bytecode_cache': {
                'name': 'default',
                'backend': 'django_jinja.cache.BytecodeCache',
                'enabled': False,
            },
            'autoescape': True,
            'auto_reload': DEBUG,
            'translation_engine': 'django.utils.translation',
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'olreg.views.global_setting',
            ],
        },
    },
    # {
    #     'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #     'DIRS': [os.path.join(BASE_DIR, 'templates')],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.request',
    #             'django.contrib.auth.context_processors.auth',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     },
    # },
]

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')]
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'heqian.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

use_local_db = 0
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if use_local_db:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'heqian',
                'USER': 'root',
                'PASSWORD': 'bb12345',
                'HOST': 'localhost',
                'PORT': 3306,
            }
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'heqian',
            'USER': 'root',
            'PASSWORD': 'heqian',
            'HOST': '39.107.226.248',
            'PORT': 3306,
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# 自定义用户模型
AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 静态文件目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = '/home/workspace/heqian/heqian/static1'

# 上传文件设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 微信配置
APPID = 'wx577571290c3830d3'
APPSECRET = '1be8a7e3173b1bc54f51d162b65d8fff'
TOKEN = "heqianyiliao"
ENCRYPT_MODE = "normal"
ENCODING_AES_KEY = "7cL65X3v9cjUAnksm3DfdONajnHLKBWCkD0ky9n7B6f"
HOST = "www.52ky.net"
#商户id
MCHID = "1517767451"

#待修改
PAY_KEY = "RIKrrMPqEKaGj23t5YvyNujZ0LaiuBzA"




# 微信公众号菜单数据
MENU_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx577571290c3830d3&redirect_uri=%s&response_type=code&scope=snsapi_base&state=123#wechat_redirect'
MENU_DATA = {
            'button':[
                {
                    'name': '看病挂号',
                    'sub_button': [
                        {
                            'type': 'view',
                            'name': '在线挂号',
                            'url': MENU_URL % ('http://%s/wx/hospital_list/' % HOST)
                        },{
                            'type': 'view',
                            'name': '我的挂号',
                            'url': MENU_URL % ('http://%s/wx/register_history_list/' % HOST)
                        }]
                },{
                    'name': '禾乾官网',
                    'sub_button': [
                        {
                            'type': 'view',
                            'name': '医馆介绍',
                            'url': MENU_URL % ('http://%s/wx/hospital_intr/' % HOST)
                        },{
                            'type': 'view',
                            'name': '医生简介',
                            'url': MENU_URL % ('http://%s/wx/doctor_intr/' % HOST)
                        },{
                            'type': 'view',
                            'name': '医馆文化',
                            'url': MENU_URL % ('http://%s/wx/hospital_know/' % HOST)
                        },{
                            'type': 'view',
                            'name': '医馆项目',
                            'url': MENU_URL % ('http://%s/wx/developing/' % HOST)
                        },{
                            'type': 'view',
                            'name': '养生小知识',
                            'url': MENU_URL % ('http://%s/wx/developing/' % HOST)
                        }]
                },{
                    'name': '我的',
                    'sub_button': [
                        {
                            'type': 'view',
                            'name': '个人中心',
                            'url': MENU_URL % ('http://%s/wx/developing/' % HOST)
                        },{
                            'type': 'view',
                            'name': '联系禾乾',
                            'url': MENU_URL % ('http://%s/wx/developing/' % HOST)
                        }]
                }
            ]}