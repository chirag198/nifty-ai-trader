"""
Celery configuration for nifty-ai-trader project.

This module sets up Celery for asynchronous task processing.
"""

import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

app = Celery('nifty_ai_trader')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Celery Beat Schedule for periodic tasks
app.conf.beat_schedule = {
    # Fetch stock prices during market hours (9:15 AM - 3:30 PM IST, Mon-Fri)
    'fetch-prices-during-market-hours': {
        'task': 'apps.stocks.tasks.fetch_all_active_stocks',
        'schedule': crontab(
            minute='*/15',  # Every 15 minutes
            hour='9-15',    # Market hours: 9 AM - 3 PM
            day_of_week='mon,tue,wed,thu,fri'  # Weekdays only
        ),
        'options': {
            'expires': 300,  # Task expires after 5 minutes if not executed
        }
    },

    # Check all active alerts every 5 minutes
    'check-all-alerts': {
        'task': 'apps.alerts.tasks.check_all_alerts',
        'schedule': crontab(minute='*/5'),
        'options': {
            'expires': 60,
        }
    },

    # Send daily market digest at 4 PM IST
    'daily-market-digest': {
        'task': 'apps.telegram_bot.tasks.send_daily_digest',
        'schedule': crontab(
            hour=16,      # 4 PM
            minute=0,
            day_of_week='mon,tue,wed,thu,fri'
        ),
    },

    # Clean up expired AI analysis cache at 2 AM daily
    'cleanup-expired-cache': {
        'task': 'apps.ai_analyzer.tasks.cleanup_expired_cache',
        'schedule': crontab(hour=2, minute=0),
    },

    # Generate usage report at midnight
    'daily-usage-report': {
        'task': 'apps.analytics.tasks.generate_daily_report',
        'schedule': crontab(hour=0, minute=0),
    },
}

# Celery configuration
app.conf.update(
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task to test Celery setup."""
    print(f'Request: {self.request!r}')
