from celery import shared_task


@shared_task
def fetch_all_active_stocks():
    """Fetch prices for all active stocks - to be implemented in Day 4."""
    pass
