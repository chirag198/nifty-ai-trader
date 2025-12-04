from django.contrib import admin
from django.utils.html import format_html
from .models import Stock, StockPrice


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    """Admin interface for Stock model."""

    list_display = [
        'symbol',
        'company_name',
        'sector',
        'is_nifty50',
        'is_active',
        'latest_price_display',
        'updated_at'
    ]
    list_filter = ['is_nifty50', 'is_active', 'sector']
    search_fields = ['symbol', 'company_name', 'nse_symbol']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']
    list_per_page = 50

    fieldsets = (
        ('Stock Information', {
            'fields': ('symbol', 'nse_symbol', 'company_name', 'sector')
        }),
        ('Status', {
            'fields': ('is_nifty50', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['activate_stocks', 'deactivate_stocks', 'mark_as_nifty50']

    def latest_price_display(self, obj):
        """Display latest price with formatting."""
        price = obj.get_latest_price()
        if price:
            return format_html('<strong>₹{:,.2f}</strong>', price)
        return format_html('<span style="color: gray;">No data</span>')
    latest_price_display.short_description = 'Latest Price'

    def activate_stocks(self, request, queryset):
        """Custom action to activate selected stocks."""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} stocks activated.')
    activate_stocks.short_description = 'Activate selected stocks'

    def deactivate_stocks(self, request, queryset):
        """Custom action to deactivate selected stocks."""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} stocks deactivated.')
    deactivate_stocks.short_description = 'Deactivate selected stocks'

    def mark_as_nifty50(self, request, queryset):
        """Mark selected stocks as Nifty 50."""
        updated = queryset.update(is_nifty50=True)
        self.message_user(request, f'{updated} stocks marked as Nifty 50.')
    mark_as_nifty50.short_description = 'Mark as Nifty 50'


@admin.register(StockPrice)
class StockPriceAdmin(admin.ModelAdmin):
    """Admin interface for StockPrice model."""

    list_display = [
        'stock',
        'timestamp',
        'open_price_display',
        'high_price_display',
        'low_price_display',
        'close_price_display',
        'volume_display',
        'change_display'
    ]
    list_filter = ['timestamp', 'stock']
    search_fields = ['stock__symbol', 'stock__company_name']
    readonly_fields = ['created_at', 'price_change', 'price_change_percent']
    date_hierarchy = 'timestamp'
    list_per_page = 100

    fieldsets = (
        ('Stock & Time', {
            'fields': ('stock', 'timestamp')
        }),
        ('Price Data', {
            'fields': ('open_price', 'high_price', 'low_price', 'close_price', 'volume')
        }),
        ('Calculated Fields', {
            'fields': ('price_change', 'price_change_percent'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def open_price_display(self, obj):
        return format_html('₹{:,.2f}', obj.open_price)
    open_price_display.short_description = 'Open'
    open_price_display.admin_order_field = 'open_price'

    def high_price_display(self, obj):
        return format_html('₹{:,.2f}', obj.high_price)
    high_price_display.short_description = 'High'
    high_price_display.admin_order_field = 'high_price'

    def low_price_display(self, obj):
        return format_html('₹{:,.2f}', obj.low_price)
    low_price_display.short_description = 'Low'
    low_price_display.admin_order_field = 'low_price'

    def close_price_display(self, obj):
        return format_html('₹{:,.2f}', obj.close_price)
    close_price_display.short_description = 'Close'
    close_price_display.admin_order_field = 'close_price'

    def volume_display(self, obj):
        """Display volume with Indian number formatting."""
        if obj.volume >= 10000000:  # 1 crore
            return format_html('{:.2f} Cr', obj.volume / 10000000)
        elif obj.volume >= 100000:  # 1 lakh
            return format_html('{:.2f} L', obj.volume / 100000)
        else:
            return format_html('{:,}', obj.volume)
    volume_display.short_description = 'Volume'
    volume_display.admin_order_field = 'volume'

    def change_display(self, obj):
        """Display price change with color coding."""
        change = obj.price_change
        change_percent = obj.price_change_percent

        if change > 0:
            color = 'green'
            symbol = '▲'
        elif change < 0:
            color = 'red'
            symbol = '▼'
        else:
            color = 'gray'
            symbol = '•'

        return format_html(
            '<span style="color: {};">{} ₹{:,.2f} ({:+.2f}%)</span>',
            color, symbol, abs(change), change_percent
        )
    change_display.short_description = 'Change'
