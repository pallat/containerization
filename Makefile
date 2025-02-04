notini:
	docker run -ti --rm ubuntu:16.04 /bin/bash
	# ps -fA
tini:
	docker run -ti --init --rm ubuntu:16.04 /bin/bash