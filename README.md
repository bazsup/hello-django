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