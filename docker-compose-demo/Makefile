.PHONY: up down logs test status status-health

up:
	mkdir -p www
	echo "<h1>Demo Docker Compose</h1>" > www/index.html
	docker compose up -d --build

logs:
	docker compose logs --tail=50 --follow

test:
	@echo "Web: http://localhost:8080"
	@echo "API: http://localhost:5001/users"
	@curl -fsS http://localhost:8080 | head -n 3 || true
	@curl -fsS http://localhost:5001/users | head -n 3 || true

status:
	@echo "Compose service status"
	docker compose ps --format '{{.Name}}\t{{.Service}}\t{{.State}}\t{{.Ports}}'

status-health:
	@echo "Compose service health details (if available)"
	@docker compose ps --quiet | xargs -I {} sh -c 'printf "%s: %s\n" "{}" "$(docker inspect --format "{{.Name}} {{.State.Status}} {{if .State.Health}}{{.State.Health.Status}}{{else}}no-health{{end}}" {})"'

down:
	docker compose down -v
