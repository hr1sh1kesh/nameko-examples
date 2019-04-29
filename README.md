# Nameko grpc Examples

## Prerequisites

* [Python 3](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/)
* Either [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) or [microk8s] (https://microk8s.io/)

## Overview

### Repository structure

There are 2 Nameko services: `Products` and `Orders` in one repository.

### Services

![Services](diagram.png)

#### Products Service

Responsible for storing and managing product information and exposing RPC Api that can be consumed by other services. This service is using Redis as it's data store. Example includes implementation of Nameko's [DependencyProvider](https://nameko.readthedocs.io/en/stable/key_concepts.html#dependency-injection) `Storage` which is used for talking to Redis.

#### Orders Service

Responsible for storing and managing orders information and exposing RPC Api that can be consumed by other services.

This service is using PostgreSQL database to persist order information.
- [nameko-sqlalchemy](https://pypi.python.org/pypi/nameko-sqlalchemy)  dependency is used to expose [SQLAlchemy](http://www.sqlalchemy.org/) session to the service class.
- [Alembic](https://pypi.python.org/pypi/alembic) is used for database migrations.

## Running examples

Set the following environment variables `CONTEXT`, `NAMESPACE` and `DOCKER_HUB_ORG` before running 

`make build-images push-images deploy-dependencies deploy-services`

This will deploy the required depdencies; Redis, Postgres and RabbitMQ onto the kubernetes cluster via helm charts. 

* > Note: Currently the passwords for rabbit, postgres and redis are hardcoded in the config as well as the helm install commands since this is just an example. 