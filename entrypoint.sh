#!/bin/sh

pip install -r requirements.txt

cd hello-django

python manage.py migrate
python manage.py runserver 0.0.0.0:8000