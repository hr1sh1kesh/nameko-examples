CONTEXT ?= microk8s
NAMESPACE ?= examples
TAG ?= latest
DOCKER_HUB_ORG ?= hrishi

deploy-namespace:
	kubectl --context=$(CONTEXT) apply -f namespace.yaml

# helm

test-chart:
	helm upgrade examples-$(SERVICE_NAME) charts/$(SERVICE_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context $(CONTEXT) \
	--dry-run --debug \
	--set image.tag=$(TAG) \
	--set image.org=$(DOCKER_HUB_ORG)

install-chart:
	helm upgrade examples-$(SERVICE_NAME) charts/$(SERVICE_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
	--set image.tag=$(TAG) \
	--set image.org=$(DOCKER_HUB_ORG)

lint-chart:
	helm lint $(SERVICE_NAME) --strict

install-gateway:
	SERVICE_NAME=gateway $(MAKE) install-chart

install-orders:
	SERVICE_NAME=orders $(MAKE) install-chart

install-products:
	SERVICE_NAME=products $(MAKE) install-chart
