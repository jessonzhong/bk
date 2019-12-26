"""
Django settings for bk project.

Generated by 'django-admin startproject' using Django 1.11.11.

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
SECRET_KEY = 'f7n$+=l+21&s5bvr63$b-jg41%#pns2rw8r*2be*km*&@g&i-1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
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

ROOT_URLCONF = 'bk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'bk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bk',
        'USER': 'root',
        'PASSWORD': 'jessonzhong',
        'HOST': '127.0.0.1',
        'PORT': 3306
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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 用户认证表默认用UserInfo表
AUTH_USER_MODEL = 'blog.UserInfo'

# 用户上传的文件都放在media文件夹中
MEDIA_DIR = "/media/"
# media配置，用户上传的文件默认放在该目录下
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 博客日志配置
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")

LOGGING = {
    'version': 1,  # 保留的参数，默认为1
    'disable_existing_loggers': False,  # 是否禁用已经存在的logger示例，设置为不禁用

    'formatters': {

        # 定义一个标准的日志格式化
        'standard': {
            'format': '[%(ascTime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelName)s][%(message)s]'
        },

        # 定义一个简单的日志格式化
        'simple': {
            'format': '[%(levelName)s][%(ascTime)s][%(filename)s:%(lineno)d]%(message)s'
        },

        # 定义一个特殊的日志格式化
        'collect': {
            'format': '%(message)s'
        },
    },

    # 过滤器
    'filters': {
        # 只有在debug=True的过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    # 处理器
    'handlers': {
        # 定义一个专门往终端打印日志的控制器
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  # 使用class类去处理日志流
            'formatter': 'simple'
        },
    },

    # 定义一个默认的日志处理器
    'default': {
        'level': 'INFO',
        'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
        'filename': os.path.join(BASE_LOG_DIR, "bk_info.log"),
        'maxBytes': 1024 * 1024 * 50,  # 日志大小：50M
        'backupCount': 5,  # 备份数量为5
        'formatter': 'standard',
        'encoding': 'utf-8',
    },

    # 定义一个专门收集错误日志的处理器
    'error': {
        'level': 'INFO',
        'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
        'filename': os.path.join(BASE_LOG_DIR, "bk_err.log"),
        'maxBytes': 1024 * 1024 * 50,  # 日志大小：50M
        'backupCount': 5,  # 备份数量为5
        'formatter': 'standard',
        'encoding': 'utf-8',
    },

    # 'loggers': {
    #     '': {
    #         'handlers': ['default', 'console', 'error'],
    #         'level': 'DEBUG',
    #         'propagate': True,  # 表示如果有父级的logger实例，要不要向上传递日志流
    #     },
    # },
}
