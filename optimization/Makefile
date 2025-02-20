normal:
	time docker build -t normal --no-cache -f normal.Dockerfile .
slim:
	time docker build -t slim --no-cache -f slim.Dockerfile .
show:
	docker images --filter "reference=*normal*" --filter "reference=*slim*"
dive:
	docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive:latest normal