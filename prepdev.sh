#! /usr/bin/env bash

while (( $# > 0 )); do
    case "${1}" in
        -d|--database)
            sudo docker run --name postgres -e POSTGRES_USERNAME=postgres -e POSTGRES_PASSWORD=cabbage -p 5432:5432 -d postgres:16-alpine
            exit 0
        ;;
        -i|--init)
            source cabbage.dev.env
            python3 manage.py createsuperuser --email "${DJANGO_SUPERUSER_EMAIL}" --full_name "${DJANGO_SUPERUSER_FULL_NAME}"
            exit 0
        ;;
        *)
            echo "Unknown argument: $1."
            exit 1
        ;;
    esac
done

python3 manage.py migrate
python3 manage.py runserver
