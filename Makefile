HTMLCOV_DIR ?= htmlcov

IMAGES ?= orders products
TAG ?= $(shell git rev-parse HEAD)

CONTEXT ?= microk8s
NAMESPACE ?= examples

DOCKER_HUB_ORG ?= hrishi
# test

coverage-html:
	coverage html -d $(HTMLCOV_DIR) --fail-under 100

coverage-report:
	coverage report -m

products-proto:
	python -m grpc_tools.protoc \
	--proto_path=proto \
	--python_out=products/products \
	--grpc_python_out=products/products \
	products.proto
	@# Hack untill I figure how to invoke this piece of code:
	@# https://github.com/grpc/grpc/pull/10862/files
	@sed -i.bak 's/^\(import.*_pb2\)/from . \1/' products/products/*grpc.py
	@rm products/products/*.bak

	python -m grpc_tools.protoc \
	--proto_path=proto \
	--python_out=orders/orders \
	--grpc_python_out=orders/orders \
	products.proto
	@# Hack untill I figure how to invoke this piece of code:
	@# https://github.com/grpc/grpc/pull/10862/files
	@sed -i.bak 's/^\(import.*_pb2\)/from . \1/' products/products/*grpc.py
	@rm products/products/*.bak

orders-proto:
	python -m grpc_tools.protoc \
	--proto_path=proto \
	--python_out=orders/orders \
	--grpc_python_out=orders/orders \
	orders.proto
	@# Hack untill I figure how to invoke this piece of code:
	@# https://github.com/grpc/grpc/pull/10862/files
	@sed -i.bak 's/^\(import.*_pb2\)/from . \1/' orders/orders/*grpc.py
	@rm orders/orders/*.bak

proto: products-proto orders-proto

test:
	flake8 orders products gateway
	coverage run -m pytest gateway/test $(ARGS)
	coverage run --append -m pytest orders/test $(ARGS)
	coverage run --append -m pytest products/test $(ARGS)

coverage: test coverage-report coverage-html

# docker

build-example-base:
	docker build -t nameko-example-base -f docker/docker.base .;

build-wheel-builder: build-example-base
	docker build -t nameko-example-builder -f docker/docker.build .;

run-wheel-builder: build-wheel-builder
	for image in $(IMAGES) ; do make -C $$image run-wheel-builder; done

build-images: run-wheel-builder
	for image in $(IMAGES) ; do TAG=$(TAG) DOCKER_HUB_ORG=$(DOCKER_HUB_ORG) make -C $$image build-image; done

push-images:
	for image in $(IMAGES) ; do make -C $$image TAG=$(TAG) DOCKER_HUB_ORG=$(DOCKER_HUB_ORG) push-image; done

build: build-images push-images

deploy-postgresql:
	helm upgrade $(NAMESPACE)-postgresql stable/postgresql \
    --install --namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
    --set fullnameOverride=postgresql \
    --set postgresqlPassword=secretpassword \
    --set postgresqlDatabase=my-database \
    --set readinessProbe.initialDelaySeconds=60 \
    --set livenessProbe.initialDelaySeconds=60

deploy-redis:
	helm upgrade $(NAMESPACE)-redis stable/redis \
    --install --namespace $(NAMESPACE) --kube-context=$(CONTEXT) \
    --set fullnameOverride=redis \
    --set password=secretpassword \
    --set cluster.enabled=false

deploy-rabbitmq:
	helm upgrade $(NAMESPACE)-rabbitmq stable/rabbitmq-ha \
    --install --namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
    --set fullnameOverride=rabbitmq \
    --set replicaCount=1 \
    --set rabbitmqUsername=admin \
    --set rabbitmqPassword=secretpassword \
    --set persistentVolume.enabled=true \
    --set updateStrategy=RollingUpdate \
    --set rabbitmqMemoryHighWatermarkType=relative \
    --set rabbitmqMemoryHighWatermark=0.5

deploy-dependencies: deploy-postgresql deploy-redis deploy-rabbitmq

deploy-services:
	for image in $(IMAGES) ; do TAG=$(TAG) DOCKER_HUB_ORG=$(DOCKER_HUB_ORG) make -C k8s install-$$image; done