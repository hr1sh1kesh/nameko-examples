#!/bin/bash

# Check if rabbit is up and running before starting the service.

is_ready() {
    eval "curl -I http://${RABBIT_USER}:${RABBIT_PASSWORD}@${RABBIT_HOST}:${RABBIT_MANAGEMENT_PORT}/api/vhosts"
}

i=0
while ! is_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - rabbit still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for rabbit to be ready"
    sleep 3
done

    while ! pg_isready -h postgresql; do echo "waiting for db"; sleep 5; done && \
    PGPASSWORD=secretpassword PGUSER=postgres PGHOST=postgresql \
    psql -tc "SELECT 1 FROM pg_database WHERE datname = 'orders'" | \
    grep -q 1 || PGPASSWORD=secretpassword PGUSER=postgres PGHOST=postgresql \
    psql -c "CREATE DATABASE orders" && \
    alembic upgrade head && \
# Run Migrations

alembic upgrade head

# Run Service

nameko run --config config.yml orders.service --backdoor 3000
