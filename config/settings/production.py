"""
Production settings for nifty-ai-trader project.
"""

from .base import *

# Debug mode is OFF in production
DEBUG = False

# SECURITY WARNING: Update this with your actual domain
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS-related settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Production logging - log to file
LOGGING['handlers']['file']['level'] = 'WARNING'
LOGGING['root']['handlers'] = ['file', 'console']

# Static files - use WhiteNoise or similar in production
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
