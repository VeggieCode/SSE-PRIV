#!/bin/sh

set -e

python -u manage.py wait_for_db
python -u manage.py collectstatic --noinput
python -u manage.py migrate

gunicorn --bind :8000 seguimiento_egresados.wsgi:application --reload