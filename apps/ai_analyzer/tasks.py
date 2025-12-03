from celery import shared_task


@shared_task
def cleanup_expired_cache():
    """Clean up expired AI analysis cache - to be implemented in Day 10."""
    pass
