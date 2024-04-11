#! /usr/bin/env bash

/opt/env/bin/python manage.py makemigrations accounts
/opt/env/bin/python manage.py makemigrations babysitters
/opt/env/bin/python manage.py migrate
/opt/env/bin/python manage.py collectstatic --no-input
/usr/sbin/nginx 
/opt/env/bin/gunicorn --worker-tmp-dir /dev/shm/ --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock core.wsgi:application --bind "0.0.0.0:8085"