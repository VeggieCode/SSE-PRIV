#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate

gunicorn --bind :8000 seguimiento_egresados.wsgi:application --reload