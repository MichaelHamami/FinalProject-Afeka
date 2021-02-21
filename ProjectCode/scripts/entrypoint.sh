#!/bin/sh

set -e
set -x

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate home && python manage.py migrate --database="problems_db" learn && python manage.py migrate --database="problems_db" problems && python manage.py migrate users && python manage.py migrate admin && python manage.py migrate auth && python manage.py migrate contenttypes && python manage.py migrate sessions && python manage.py migrate sites

# Start server
echo "Starting server"
#python manage.py runserver 0.0.0.0:8000
python manage.py runsslserver 0.0.0.0:8000