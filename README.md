### django_api-library - A demo of basic Django API functionality using Django Rest Framework(DRF)

---
### Features
 - Basic browseable API
 - TBD

### Installation
 - `git clone https://github.com/kevinbowen777/django_api-library.git`
 - `cd django_api-library`
 - Local installation:
     - `mkvirtualenv django_api-library` or  `workon django_api-library`
     - `poetry install`
     - `poetry run python manage.py runserver`
 - Docker container:
     - `docker-compose up --build`
     - `docker-compose exec web python manage.py migrate`
     - `docker-compose exec web python manage.py createsuperuser`
 - URLs:
    - http://127.0.0.1:8000/api/v1/
    - http://127.0.0.1:8000/api/v1/1/?format=json
    - https://kbowen-django-api-library.herokuapp.com/api/v1/

### Live Demo on Heroku:
 - [django-api-library](https://kbowen-django-api-library.herokuapp.com/)


---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/django_api-library/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_api-library/issues)
      to view currently open bug reports or open a new issue.
