.PHONY: up up-worker down logs test

up:
	docker compose up -d --build

up-worker:
	docker compose --profile worker up -d --build

logs:
	docker compose logs --follow

test:
	@echo "web -> http://localhost:8080"
	@echo "api -> http://localhost:5002/users"
	@curl -fsS http://localhost:5002/users | head -n 3 || true

down:
	docker compose down -v
