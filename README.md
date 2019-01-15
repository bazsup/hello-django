# Hello Django


Start Development server using
```bash
python manage.py runserver
```

## Migration

- after change model
```
python manage.py makemigrations
```

- migrate table
```
python manage.py migrate
```

### Create superuser

- create superuser for create admin
```
python manage.py createsuperuser
```

## Testing

- run test
```
python manage.py migrate
```

- run test specific file
```
python manage.py <file-name>
```

## Test coverage

you need to see test coverage
- install coverage by using this command
```
pip install coverage
```

run test first
```
coverage run manage.py test
```

show report
```
coverage report
```

## Docker

If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:
```
sudo usermod -aG docker your-user
```

start this application by using
```
docker-compose up
```

## Generate ssh-key
```
ssh-keygen -t rsa -C "<your@email>"
```