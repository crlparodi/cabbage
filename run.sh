#! /usr/bin/env bash

/opt/env/bin/python manage.py collectstatic --no-input
/opt/env/bin/gunicorn --bind 0.0.0.0:5000 core.wsgi:application