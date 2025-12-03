.PHONY: help install runserver migrate makemigrations createsuperuser shell test clean docker-up docker-down docker-logs celery-worker celery-beat lint format

help:
	@echo "Nifty AI Trader - Available Commands:"
	@echo ""
	@echo "Development:"
	@echo "  make install          - Install Python dependencies"
	@echo "  make runserver        - Run Django development server"
	@echo "  make shell            - Open Django shell"
	@echo "  make createsuperuser  - Create Django superuser"
	@echo ""
	@echo "Database:"
	@echo "  make migrate          - Run database migrations"
	@echo "  make makemigrations   - Create new migrations"
	@echo ""
	@echo "Celery:"
	@echo "  make celery-worker    - Start Celery worker"
	@echo "  make celery-beat      - Start Celery beat scheduler"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-up        - Start all Docker services"
	@echo "  make docker-down      - Stop all Docker services"
	@echo "  make docker-logs      - Show Docker logs"
	@echo "  make docker-build     - Build Docker images"
	@echo ""
	@echo "Testing & Quality:"
	@echo "  make test             - Run test suite with coverage"
	@echo "  make lint             - Run code linters"
	@echo "  make format           - Format code with black and isort"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean            - Remove Python artifacts"
	@echo "  make seed             - Seed Nifty50 stock data"

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

runserver:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

shell:
	python manage.py shell_plus

test:
	pytest -v --cov=apps --cov-report=html --cov-report=term

celery-worker:
	celery -A config worker -l info

celery-beat:
	celery -A config beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

docker-build:
	docker-compose build

docker-restart:
	docker-compose restart

lint:
	flake8 .
	mypy .

format:
	black .
	isort .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true

seed:
	python manage.py seed_nifty50

backfill:
	python scripts/backfill_prices.py
