from django.db import models
from django.utils import timezone


class Stock(models.Model):
    """Model to store Indian stock information."""

    symbol = models.CharField(
        max_length=20,
        unique=True,
        help_text="Stock symbol (e.g., RELIANCE)"
    )
    nse_symbol = models.CharField(
        max_length=20,
        unique=True,
        help_text="NSE symbol for yfinance (e.g., RELIANCE.NS)"
    )
    company_name = models.CharField(
        max_length=200,
        help_text="Full company name"
    )
    sector = models.CharField(
        max_length=100,
        blank=True,
        help_text="Industry sector"
    )
    is_nifty50 = models.BooleanField(
        default=False,
        help_text="Is this stock part of Nifty 50 index?"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Is this stock actively tracked?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'stocks'
        ordering = ['symbol']
        indexes = [
            models.Index(fields=['symbol'], name='idx_stock_symbol'),
            models.Index(fields=['is_nifty50'], name='idx_stock_nifty50'),
            models.Index(fields=['is_active'], name='idx_stock_active'),
        ]

    def __str__(self):
        return f"{self.symbol} - {self.company_name}"

    def get_latest_price(self):
        """Get the most recent price for this stock."""
        latest = self.prices.order_by('-timestamp').first()
        return latest.close_price if latest else None

    def get_previous_close(self):
        """Get the previous day's closing price."""
        prices = self.prices.order_by('-timestamp')[:2]
        if len(prices) == 2:
            return prices[1].close_price
        return None


class StockPrice(models.Model):
    """Model to store historical stock price data."""

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='prices'
    )
    timestamp = models.DateTimeField(
        help_text="Time of price data"
    )
    open_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Opening price"
    )
    high_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Highest price"
    )
    low_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Lowest price"
    )
    close_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Closing price"
    )
    volume = models.BigIntegerField(
        help_text="Trading volume"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stock_prices'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['stock', '-timestamp'], name='idx_price_stock_time'),
            models.Index(fields=['timestamp'], name='idx_price_timestamp'),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['stock', 'timestamp'],
                name='unique_stock_timestamp'
            )
        ]

    def __str__(self):
        return f"{self.stock.symbol} - {self.timestamp.strftime('%Y-%m-%d %H:%M')} - ₹{self.close_price}"

    @property
    def price_change(self):
        """Calculate price change from open to close."""
        return self.close_price - self.open_price

    @property
    def price_change_percent(self):
        """Calculate percentage price change."""
        if self.open_price > 0:
            return ((self.close_price - self.open_price) / self.open_price) * 100
        return 0
