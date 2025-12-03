from celery import shared_task


@shared_task
def send_daily_digest():
    """Send daily market digest to subscribers - to be implemented in Day 13."""
    pass
