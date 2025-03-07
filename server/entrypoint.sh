#!/bin/sh

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python3 manage.py makemigrations djangoapp --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec "$@"