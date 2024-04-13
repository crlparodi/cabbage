#! /usr/bin/env bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"admin@example.com"}
SUPERUSER_FULL_NAME=${DJANGO_SUPERUSER_FULL_NAME:-"Mister Admin"}
# cd /usr/src/cabbage

/opt/env/bin/python manage.py migrate --no-input
/opt/env/bin/python manage.py createsuperuser --email ${SUPERUSER_EMAIL} --full_name "${SUPERUSER_FULL_NAME}" --no-input || true
