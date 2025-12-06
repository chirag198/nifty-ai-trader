![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=Django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=PostgreSQL&logoColor=white)
![AI](https://img.shields.io/badge/-Claude%20AI-10A37F?style=flat-square&logo=OpenAI&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

# Nifty AI Trader

AI-powered stock tracking and trading recommendations for Indian Nifty stocks using Claude API.

## Overview

Nifty AI Trader is a hobby project that combines AI-powered analysis with real-time stock market data for Indian Nifty stocks. It provides:

- **Stock Price Tracking**: Automated fetching of Nifty stock prices during market hours
- **Smart Alerts**: Price-based and percentage-change alerts
- **AI Recommendations**: Buy/Sell/Hold recommendations powered by Claude AI
- **Telegram Bot**: Interact with your trading assistant via Telegram
- **Cost Optimization**: Intelligent caching to minimize API costs (<$5/month)

## Tech Stack

- **Backend**: Django 5.0, Django REST Framework
- **Database**: PostgreSQL 15
- **Task Queue**: Celery with Redis
- **AI**: Anthropic Claude API (Haiku & Sonnet models)
- **Stock Data**: yfinance (free Indian stock data)
- **Messaging**: python-telegram-bot
- **Deployment**: Docker & Docker Compose

## Project Status

**Day 1 Complete**: Initial project setup with Django, Docker, PostgreSQL, Redis, and Celery configuration.

### Completed
- ✅ Django project structure with split settings (dev/prod)
- ✅ Docker Compose setup (PostgreSQL + Redis)
- ✅ Celery configuration with beat scheduler
- ✅ Django apps scaffolding (stocks, alerts, ai_analyzer, telegram_bot, analytics)
- ✅ Makefile with common commands
- ✅ Environment configuration

### Coming Next (Day 2)
- Stock and StockPrice models
- Django admin interface
- Nifty50 seed data

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/cgulati198/nifty-ai-trader.git
cd nifty-ai-trader
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
make install
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - ANTHROPIC_API_KEY
# - TELEGRAM_BOT_TOKEN
```

5. **Start Docker services**
```bash
make docker-up
```

6. **Run migrations**
```bash
python manage.py migrate
```

7. **Create superuser**
```bash
make createsuperuser
```

8. **Run development server**
```bash
make runserver
```

Visit http://localhost:8000/admin to access the Django admin panel.

## Development Workflow

### Running Services

**Development Server**:
```bash
make runserver
```

**Celery Worker** (in separate terminal):
```bash
make celery-worker
```

**Celery Beat Scheduler** (in separate terminal):
```bash
make celery-beat
```

### Docker Commands

```bash
make docker-up        # Start all services
make docker-down      # Stop all services
make docker-logs      # View logs
make docker-build     # Rebuild images
```

### Database Commands

```bash
make migrate          # Run migrations
make makemigrations   # Create new migrations
make shell            # Django shell
```

### Testing & Code Quality

```bash
make test             # Run tests with coverage
make lint             # Run linters
make format           # Format code with black and isort
```

## Project Structure

```
nifty-ai-trader/
├── apps/
│   ├── stocks/          # Stock data management
│   ├── alerts/          # Price alert system
│   ├── ai_analyzer/     # AI-powered analysis
│   ├── telegram_bot/    # Telegram integration
│   └── analytics/       # Usage & cost tracking
├── config/
│   ├── settings/        # Django settings (base, dev, prod)
│   ├── celery.py        # Celery configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py
├── scripts/             # Management scripts
├── docs/                # Documentation
├── docker-compose.yml   # Docker services
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

## Environment Variables

Key environment variables (see .env.example for complete list):

```bash
# Django
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True

# Database
DATABASE_URL=postgresql://postgres:postgres@db:5432/nifty_ai_trader

# APIs
ANTHROPIC_API_KEY=your-claude-api-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token

# AI Settings
AI_DEFAULT_MODEL=claude-3-haiku-20240307
AI_CACHE_HOURS=6
```

## Roadmap

### Phase 1: Foundation (Days 1-3) ✅
- Day 1: Project setup ✅
- Day 2: Stock models & admin
- Day 3: yfinance integration

### Phase 2: Automation (Days 4-5)
- Day 4: Scheduled price updates
- Day 5: Historical data backfill

### Phase 3: Alerts (Days 6-7)
- Day 6: Alert models & logic
- Day 7: Alert processing & notifications

### Phase 4: AI Integration (Days 8-10)
- Day 8: Claude API client
- Day 9: Analysis engine & prompts
- Day 10: Cost optimization & dashboard

### Phase 5: Telegram Bot (Days 11-13)
- Day 11: Basic bot commands
- Day 12: Alert management via Telegram
- Day 13: AI analysis commands

### Phase 6: Polish (Days 14-15)
- Day 14: Comprehensive testing
- Day 15: Documentation & deployment

## Cost Optimization

**Budget**: $20/month Claude API subscription
**Target**: <$5/month actual usage

### Strategies
- Aggressive caching (6-12 hour validity)
- Use Claude 3 Haiku for routine analysis (90%)
- Claude 3.5 Sonnet only for critical decisions (10%)
- Rate limiting (100 analyses/day max)
- Smart triggers (only analyze significant price movements)

**Estimated Cost**: ~$0.35-$1/month with proper caching

## Contributing

This is a personal hobby project, but suggestions and feedback are welcome!

## License

MIT License

## Disclaimer

This tool is for educational and personal use only. It is not financial advice. Always do your own research before making investment decisions. The AI recommendations are based on historical data and technical analysis, which may not predict future market behavior.

---

**Created by**: Chirag Gulati
**GitHub**: [@cgulati198](https://github.com/cgulati198)
