import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your_secret_key_here'  # Replace with a secure secret key in production

DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['*']  # Update with actual host(s) in production

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coreservice',
        'USER': 'postgres',
        'PASSWORD': 'Ahgase07',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.menu_service',
    'apps.cart_service',
    'apps.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'api.middleware.ProxyMiddleware',
]

# Proxy service URLs
MENU_SERVICE_URL = 'http://resto-menuservice:8001'  # Update with actual URL
CART_SERVICE_URL = 'http://resto-cartservice:8002'  # Update with actual URL

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# CORS settings (adjust as needed)
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins in development; set to False in production
