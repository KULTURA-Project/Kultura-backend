"""
Django settings for vegetables project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5pi8i@uv9+#ut-0%(b^ot^*zte)j#*+!0tqmm#qbg2m@xtu1$+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*' , 'https://badolo.pythonanywhere.com/']


# Application definition

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    'mptt','widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'drf_yasg',
    'rest_framework',
     "corsheaders",
    'customers',
    'vendors',
    'product',
    'orders',
    'rest_framework.authtoken',
    


]


MIDDLEWARE = [
      'django.middleware.csrf.CsrfViewMiddleware',
      "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
  
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kultura.urls'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Your React app's origin
    "http://localhost:8000",  # Your Django app's origin
]
CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
     "http://localhost:3000",
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates') ],
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


WSGI_APPLICATION = 'kultura.wsgi.application'

# settings.py

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
USERNAME_FIELD = 'email'
AUTH_USER_MODEL = 'auth.User'  # or your custom user model

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


SWAGGER_SETTINGS = {

    'VALIDATOR_URL': 'http://localhost:8000',
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Adjust this to match the structure of your static directory
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# settings.py
MEDIA_URL = '/'
MEDIA_ROOT = BASE_DIR / ''

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication backend
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _



UNFOLD = {
    "SITE_TITLE": "KULTURA Admin",
    "SITE_HEADER": "KULTURA",
    "SITE_URL": "/",
    #"SITE_ICON": lambda request: static("/LOGO-SYMBIOSE-YAAR_1.png"),
    '''  "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",
            "href": lambda request: static("/LOGO-SYMBIOSE-YAAR_1.png"),
        },
    ],'''
    #"SITE_LOGO": {
       # "sizes": "32x32",
       # "light": lambda request: static("/LOGO-SYMBIOSE-YAAR_1.png"),
       # "dark": lambda request: static("/LOGO-SYMBIOSE-YAAR_1.png"),
    #},
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "light",
    "LOGIN": {
        "redirect_after": lambda request: reverse_lazy("admin:product_product_changelist"),
    },
    "STYLES": [
        lambda request: static("css/admin_custom.css"),
    ],
    "COLORS": {
        "primary": {
            "50": "240 253 244",
            "100": "220 252 231",
            "200": "187 247 208",
            "300": "134 239 172",
            "400": "74 222 128",
            "500": "34 197 94",
            "600": "22 163 74",
            "700": "21 128 61",
            "800": "22 101 52",
            "900": "20 83 45",
            "950": "14 59 34",
        },
        "background": {
            "light": "255 255 255",
            "dark": "0 0 0",
        },
        "font": {
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "0 128 0",
            "important-dark": "255 255 255",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
          
            {
                "title": _("Admin Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Products"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:product_product_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:product_category_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Orders"),
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Customers"),
                        "icon": "people",
                        "link": reverse_lazy("admin:orders_customer_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                ],
            },
            {
                "title": _("Marketing"),
                "collapsible": True,
                "items": [
                    {
                        "title": _("Coupons"),
                        "icon": "local_offer",
                        "link": reverse_lazy("admin:orders_coupon_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Promotions"),
                        "icon": "campaign",
                        "link": reverse_lazy("admin:orders_promotion_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                    {
                        "title": _("Wishlist"),
                        "icon": "favorite",
                        "link": reverse_lazy("admin:orders_wishlist_changelist"),
                        "permission": lambda request: request.user.is_superuser,  # Admin only
                    },
                ],
            },
            {
                "title": _("Gestionnaire Admin"),
                "separator": True,
                "collapsible": False,
                "items": [
                
                    {
                        "title": _("My Products"),
                        "icon": "inventory",
                        "link": reverse_lazy("admin:product_product_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:product_category_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Orders"),
                        "icon": "shopping_cart",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Customers"),
                        "icon": "people",
                        "link": reverse_lazy("admin:orders_customer_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Wishlist"),
                        "icon": "favorite",
                        "link": reverse_lazy("admin:orders_wishlist_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Coupons"),
                        "icon": "local_offer",
                        "link": reverse_lazy("admin:orders_coupon_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Promotions"),
                        "icon": "campaign",
                        "link": reverse_lazy("admin:orders_promotion_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                    {
                        "title": _("My Transactions"),
                        "icon": "monetization_on",
                        "link": reverse_lazy("admin:orders_transaction_changelist"),
                        "permission": lambda request: request.user.groups.filter(name="Vendor").exists(),
                    },
                ],
            }
        ],
    },
}


X_FRAME_OPTIONS = 'SAMEORIGIN'


'''
     {
                        "title": "Featured Products",
                        "icon": "star",
                        "link": reverse_lazy("admin:product_product_featured_products"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                    {
                        "title": "Out-of-Stock Products",
                        "icon": "warning",
                        "link": reverse_lazy("admin:product_product_out_of_stock_products"),
                        "permission": lambda request: request.user.is_superuser,
                    },'''
                    
                    
                    
''' {
                "title": "Custom Pages",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Product List",
                        "icon": "inventory",
                        "link": reverse_lazy("admin:product_product_tools"),
                        "permission": lambda request: request.user.is_superuser,
                    },
                 
                ],
            },                    '''