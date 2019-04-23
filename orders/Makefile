TAG ?= dev
# docker
DOCKER_HUB_ORG ?= hrishi


run-wheel-builder:
	docker run --rm \
		-v "$$(pwd)":/application -v "$$(pwd)"/wheelhouse:/wheelhouse \
		nameko-example-builder;

build-image:
	docker build -t $(DOCKER_HUB_ORG)/nameko-example-orders:$(TAG) -f docker.run .;

push-image:
	docker push $(DOCKER_HUB_ORG)/nameko-example-orders:$(TAG)
