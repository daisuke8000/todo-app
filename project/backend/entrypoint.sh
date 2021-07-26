#!/bin/bash

echo "waiting for postgres"

while ! nc -z api-db 5432; do
  sleep 0.5
done

echo "PostgresSQL start!"

exec "$@"