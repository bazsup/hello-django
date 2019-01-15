#!/bin/sh

PROJECT_PATH=~/hello-django/docker-compose.prod.yml
docker-compose -f $PROJECT_PATH pull
docker-compose -f $PROJECT_PATH up -d