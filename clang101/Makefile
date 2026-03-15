IMAGE_NAME=clang101-server
CONTAINER_NAME=clang101-server
PORT=8888

.PHONY: all build run stop logs shell test clean

all: build

build:
	docker build -t $(IMAGE_NAME) .

run: stop
	docker run --rm -d \
		--name $(CONTAINER_NAME) \
		-p $(PORT):8888 \
		$(IMAGE_NAME)

stop:
	-docker stop $(CONTAINER_NAME)
	-docker rm -f $(CONTAINER_NAME) 2>/dev/null || true

logs:
	docker logs -f $(CONTAINER_NAME)

shell:
	docker exec -it $(CONTAINER_NAME) sh

test: run
	@echo "Waiting for server to start..."
	sleep 1
	curl -f http://127.0.0.1:8888 -o /tmp/clang101_api_test.txt
	if grep -q "Hello, World!" /tmp/clang101_api_test.txt; then \
		echo "API test passed"; \
		docker stop $(CONTAINER_NAME); \
		echo "Server stopped"; \
	else \
		echo "API test failed"; \
		docker stop $(CONTAINER_NAME); \
		exit 1; \
	fi

clean: stop
	docker image rm -f $(IMAGE_NAME) 2>/dev/null || true
