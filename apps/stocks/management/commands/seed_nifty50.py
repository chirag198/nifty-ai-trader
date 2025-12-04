from django.core.management.base import BaseCommand
from apps.stocks.models import Stock


class Command(BaseCommand):
    help = 'Seed the database with Nifty 50 stocks'

    # Nifty 50 stocks data (as of 2025)
    NIFTY_50_STOCKS = [
        {'symbol': 'RELIANCE', 'company_name': 'Reliance Industries Ltd.', 'sector': 'Oil & Gas'},
        {'symbol': 'TCS', 'company_name': 'Tata Consultancy Services Ltd.', 'sector': 'IT Services'},
        {'symbol': 'HDFCBANK', 'company_name': 'HDFC Bank Ltd.', 'sector': 'Banking'},
        {'symbol': 'INFY', 'company_name': 'Infosys Ltd.', 'sector': 'IT Services'},
        {'symbol': 'ICICIBANK', 'company_name': 'ICICI Bank Ltd.', 'sector': 'Banking'},
        {'symbol': 'HINDUNILVR', 'company_name': 'Hindustan Unilever Ltd.', 'sector': 'FMCG'},
        {'symbol': 'ITC', 'company_name': 'ITC Ltd.', 'sector': 'FMCG'},
        {'symbol': 'SBIN', 'company_name': 'State Bank of India', 'sector': 'Banking'},
        {'symbol': 'BHARTIARTL', 'company_name': 'Bharti Airtel Ltd.', 'sector': 'Telecom'},
        {'symbol': 'KOTAKBANK', 'company_name': 'Kotak Mahindra Bank Ltd.', 'sector': 'Banking'},
        {'symbol': 'LT', 'company_name': 'Larsen & Toubro Ltd.', 'sector': 'Construction'},
        {'symbol': 'HCLTECH', 'company_name': 'HCL Technologies Ltd.', 'sector': 'IT Services'},
        {'symbol': 'AXISBANK', 'company_name': 'Axis Bank Ltd.', 'sector': 'Banking'},
        {'symbol': 'ASIANPAINT', 'company_name': 'Asian Paints Ltd.', 'sector': 'Paints'},
        {'symbol': 'MARUTI', 'company_name': 'Maruti Suzuki India Ltd.', 'sector': 'Automobile'},
        {'symbol': 'SUNPHARMA', 'company_name': 'Sun Pharmaceutical Industries Ltd.', 'sector': 'Pharma'},
        {'symbol': 'TITAN', 'company_name': 'Titan Company Ltd.', 'sector': 'Jewellery'},
        {'symbol': 'BAJFINANCE', 'company_name': 'Bajaj Finance Ltd.', 'sector': 'NBFC'},
        {'symbol': 'ULTRACEMCO', 'company_name': 'UltraTech Cement Ltd.', 'sector': 'Cement'},
        {'symbol': 'WIPRO', 'company_name': 'Wipro Ltd.', 'sector': 'IT Services'},
        {'symbol': 'NTPC', 'company_name': 'NTPC Ltd.', 'sector': 'Power'},
        {'symbol': 'M&M', 'company_name': 'Mahindra & Mahindra Ltd.', 'sector': 'Automobile'},
        {'symbol': 'TATAMOTORS', 'company_name': 'Tata Motors Ltd.', 'sector': 'Automobile'},
        {'symbol': 'NESTLEIND', 'company_name': 'Nestle India Ltd.', 'sector': 'FMCG'},
        {'symbol': 'TATASTEEL', 'company_name': 'Tata Steel Ltd.', 'sector': 'Steel'},
        {'symbol': 'TECHM', 'company_name': 'Tech Mahindra Ltd.', 'sector': 'IT Services'},
        {'symbol': 'POWERGRID', 'company_name': 'Power Grid Corporation of India Ltd.', 'sector': 'Power'},
        {'symbol': 'ONGC', 'company_name': 'Oil and Natural Gas Corporation Ltd.', 'sector': 'Oil & Gas'},
        {'symbol': 'BAJAJFINSV', 'company_name': 'Bajaj Finserv Ltd.', 'sector': 'Financial Services'},
        {'symbol': 'DIVISLAB', 'company_name': 'Divi\'s Laboratories Ltd.', 'sector': 'Pharma'},
        {'symbol': 'ADANIPORTS', 'company_name': 'Adani Ports and Special Economic Zone Ltd.', 'sector': 'Logistics'},
        {'symbol': 'DRREDDY', 'company_name': 'Dr. Reddy\'s Laboratories Ltd.', 'sector': 'Pharma'},
        {'symbol': 'COALINDIA', 'company_name': 'Coal India Ltd.', 'sector': 'Mining'},
        {'symbol': 'EICHERMOT', 'company_name': 'Eicher Motors Ltd.', 'sector': 'Automobile'},
        {'symbol': 'JSWSTEEL', 'company_name': 'JSW Steel Ltd.', 'sector': 'Steel'},
        {'symbol': 'BRITANNIA', 'company_name': 'Britannia Industries Ltd.', 'sector': 'FMCG'},
        {'symbol': 'INDUSINDBK', 'company_name': 'IndusInd Bank Ltd.', 'sector': 'Banking'},
        {'symbol': 'HINDALCO', 'company_name': 'Hindalco Industries Ltd.', 'sector': 'Metals'},
        {'symbol': 'TATACONSUM', 'company_name': 'Tata Consumer Products Ltd.', 'sector': 'FMCG'},
        {'symbol': 'GRASIM', 'company_name': 'Grasim Industries Ltd.', 'sector': 'Cement'},
        {'symbol': 'CIPLA', 'company_name': 'Cipla Ltd.', 'sector': 'Pharma'},
        {'symbol': 'HEROMOTOCO', 'company_name': 'Hero MotoCorp Ltd.', 'sector': 'Automobile'},
        {'symbol': 'SBILIFE', 'company_name': 'SBI Life Insurance Company Ltd.', 'sector': 'Insurance'},
        {'symbol': 'BPCL', 'company_name': 'Bharat Petroleum Corporation Ltd.', 'sector': 'Oil & Gas'},
        {'symbol': 'ADANIENT', 'company_name': 'Adani Enterprises Ltd.', 'sector': 'Conglomerate'},
        {'symbol': 'APOLLOHOSP', 'company_name': 'Apollo Hospitals Enterprise Ltd.', 'sector': 'Healthcare'},
        {'symbol': 'SHRIRAMFIN', 'company_name': 'Shriram Finance Ltd.', 'sector': 'NBFC'},
        {'symbol': 'HDFCLIFE', 'company_name': 'HDFC Life Insurance Company Ltd.', 'sector': 'Insurance'},
        {'symbol': 'BAJAJ-AUTO', 'company_name': 'Bajaj Auto Ltd.', 'sector': 'Automobile'},
        {'symbol': 'LTIM', 'company_name': 'LTIMindtree Ltd.', 'sector': 'IT Services'},
    ]

    def handle(self, *args, **options):
        """Seed Nifty 50 stocks into the database."""

        self.stdout.write(self.style.NOTICE('Starting Nifty 50 stock seeding...'))

        created_count = 0
        updated_count = 0
        skipped_count = 0

        for stock_data in self.NIFTY_50_STOCKS:
            symbol = stock_data['symbol']
            nse_symbol = f"{symbol}.NS"

            # Create or update stock
            stock, created = Stock.objects.update_or_create(
                symbol=symbol,
                defaults={
                    'nse_symbol': nse_symbol,
                    'company_name': stock_data['company_name'],
                    'sector': stock_data.get('sector', ''),
                    'is_nifty50': True,
                    'is_active': True,
                }
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'  ✓ Created: {symbol} - {stock_data["company_name"]}')
                )
            else:
                # Check if it was already a Nifty 50 stock
                if stock.is_nifty50:
                    skipped_count += 1
                    self.stdout.write(
                        self.style.WARNING(f'  - Skipped: {symbol} (already exists)')
                    )
                else:
                    updated_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'  ✓ Updated: {symbol} - {stock_data["company_name"]}')
                    )

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS(f'Seeding completed!'))
        self.stdout.write(self.style.SUCCESS(f'  Created: {created_count}'))
        self.stdout.write(self.style.SUCCESS(f'  Updated: {updated_count}'))
        self.stdout.write(self.style.WARNING(f'  Skipped: {skipped_count}'))
        self.stdout.write(self.style.SUCCESS(f'  Total: {len(self.NIFTY_50_STOCKS)}'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
