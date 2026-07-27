#!/bin/sh

set -e

echo "Attendo PostgreSQL..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "PostgreSQL disponibile."

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"