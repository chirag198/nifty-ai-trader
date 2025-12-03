"""
Development settings for nifty-ai-trader project.
"""

from .base import *

# Debug mode is ON in development
DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ['*']

# Additional apps for development
INSTALLED_APPS += [
    'django_extensions',
]

# Development-specific logging
LOGGING['loggers']['apps']['level'] = 'DEBUG'

# Disable HTTPS redirects in development
SECURE_SSL_REDIRECT = False

# Django Debug Toolbar (optional - uncomment if needed)
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
# INTERNAL_IPS = ['127.0.0.1']
