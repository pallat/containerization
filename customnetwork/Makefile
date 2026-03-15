create:
	-docker network create my-app-net
	docker network inspect my-app-net >/dev/null 2>&1 || true

clean:
	-docker rm -f web db 2>/dev/null || true

# db needs required ENV so it stays up; here we set POSTGRES_PASSWORD
db: clean create
	docker run -d --name db --net my-app-net -e POSTGRES_PASSWORD=secret postgres

web: create
	docker run -d --name web --net my-app-net nginx:alpine

exec-web:
	docker exec -it web sh

# To test ping after web is running and db is up
ping-db:
	docker exec -it web sh -c "ping -c 3 db"

connect-demo:
	@echo "Demo docker network connect"
	docker network create net-a 2>/dev/null || true
	docker network create net-b 2>/dev/null || true
	docker rm -f c1 db 2>/dev/null || true
	docker run -d --name c1 --net net-a nginx:alpine
	docker run -d --name db --net net-b -e POSTGRES_PASSWORD=secret postgres
	@echo "Before connect: ping from c1 to db (should fail)"
	docker exec c1 sh -c "ping -c 1 db || true"
	@echo "Connecting c1 to net-b"
	docker network connect net-b c1
	@echo "After connect: ping from c1 to db"
	docker exec c1 sh -c "ping -c 1 db"
	@echo "Cleanup: run make connect-down when done"

connect-down:
	-docker stop c1 db
	-docker rm -f c1 db
	-docker network rm net-a net-b

down:
	-docker stop web db
	-docker rm -f web db
	-docker network rm my-app-net