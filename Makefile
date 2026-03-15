notini:
	docker run -ti --rm ubuntu:22.04 /bin/bash
	# ps -fA
tini:
	docker run -ti --init --rm ubuntu:22.04 /bin/bash