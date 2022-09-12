"""Settings for the django_api-libraries project."""
from pathlib import Path

# import socket  # noqa: E402 # Comment out if not using debug_toolbar

from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = [".herokuapp.com", "localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    # "debug_toolbar",
    "bootstrap4",
    "corsheaders",
    "crispy_forms",
    "django_countries",
    "django_extensions",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_spectacular",
    # Local
    "accounts.apps.AccountsConfig",
    "api.apps.ApiConfig",
    "books.apps.BooksConfig",
    "pages.apps.PagesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.joinpath("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "debug": True,
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL", default="postgres://postgres@db/postgres"
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa:E501,B950
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa:E501,B950
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa:E501,B950
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa:E501,B950
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Vancouver"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = (str(BASE_DIR.joinpath("static")),)
STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR.joinpath("media"))

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 5,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "django-api-library",
    "DESCRIPTION": "A basic demo of Django API functionality using DRF",
    "VERSION": "0.1.0",
}

SITE_ID = 1
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
ACCOUNT_EMAIL_VERIFICATION = "none"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
)

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

# django-debug-toolbar
# Use the following in Docker only:
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
# The following is for use locally:
# INTERNAL_IPS = ["127.0.0.1"]
