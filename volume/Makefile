VOLUME_DIR := /tmp/demo-volume
CONTAINER_NAME := volume-demo

.PHONY: all demo up down cat
all: demo

demo: up
	@echo "Visit http://localhost:8080"
	@echo "Then edit $(VOLUME_DIR)/index.html and refresh."

up:
	mkdir -p $(VOLUME_DIR)
	echo "<h1>Hello from host at $$(date)</h1>" > $(VOLUME_DIR)/index.html
	docker run --rm -d --name $(CONTAINER_NAME) -p 8080:80 \
		-v $(VOLUME_DIR):/usr/share/nginx/html:ro nginx:alpine
	@echo "Started container $(CONTAINER_NAME)"

down:
	-docker stop $(CONTAINER_NAME)
	-docker rm -f $(CONTAINER_NAME) 2>/dev/null || true
	@echo "Stopped container $(CONTAINER_NAME)"

cat:
	@echo "==== Host file content ===="
	cat $(VOLUME_DIR)/index.html
	@echo "==========================="

bind:
	@echo "Demo bind mount from host ./bind-src to container /bind-dest"
	mkdir -p ./bind-src
	echo "hello from host bind-src at $$(date)" > ./bind-src/example.txt
	docker run --rm -it -v $$(pwd)/bind-src:/bind-dest:rw ubuntu:22.04 bash -lc "ls -l /bind-dest && cat /bind-dest/example.txt"
	@echo "Now inside host, update ./bind-src/example.txt and rerun to see changes reflected in container"

volume-create:
	@echo "Demo docker managed volume create + use"
	docker volume create demo-vol
	-docker rm -f volume-create-demo 2>/dev/null || true
	docker run --rm -d --name volume-create-demo -p 8081:80 -v demo-vol:/usr/share/nginx/html:ro nginx:alpine
	@echo "Waiting 1 sec for container to start..."
	sleep 1
	@echo "Check volume contents (empty by default):"
	docker run --rm -v demo-vol:/data alpine ls -l /data || true
	@echo "Write index.html into volume using temporary container"
	docker run --rm -v demo-vol:/data alpine sh -c 'echo "<h1>Managed volume content at $$(date)</h1>" > /data/index.html'
	@echo "Now container should serve updated page on http://localhost:8081"
	@echo "Open browser or run: curl -s http://localhost:8081 | head -n 1"
	@echo "Stop and remove demo container with 'make volume-down'"

volume-check:
	@echo "=== Docker Volume + Container Status ==="
	docker ps -a --filter "name=volume-create-demo"
	@echo "=== Volume List (demo only) ==="
	docker volume ls | grep demo-vol || true
	@echo "=== Volume Inspect ==="
	docker volume inspect demo-vol || true
	@echo "=== Check served content at localhost:8081 (if container running) ==="
	curl -fsS http://localhost:8081 | head -n 1 || echo "(no response)"

volume-down:
	-docker stop volume-create-demo
	-docker rm -f volume-create-demo 2>/dev/null || true
	touch /tmp/volume-demo-end
	docker volume rm demo-vol || true
	@echo "Stopped container and removed docker volume demo-vol"

volume-clean: volume-down
	@echo "Removing demo directory and temp files"
	rm -rf $(VOLUME_DIR)
	rm -f /tmp/volume-demo-end
	@echo "Clean complete."