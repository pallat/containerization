SHELL := /bin/zsh

.PHONY: docker
docker: ## build the docker image
	@echo "Building the docker image"
	# build and replace the image
	docker build --rm -t tiniapi .

notini:
	docker run -p 8080:8080 --rm tiniapi sh -c "ls;ps;/api"
	# /api
	# docker ps
	# docker kill --signal=SIGKILL <container_id>
tini:
	docker run -ti -p 8080:8080 --init --rm tiniapi /api