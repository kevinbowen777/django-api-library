django-api-library
==================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   package_index
   create_new_users
   add_book_list

.. contents:: Table of Contents
   :local:
   :backlinks: top
   :depth: 2

A basic library website & API built with Django 5.1.x & Django REST Framework (DRF) 3.13.x

Features
--------

 * Application

   * Browseable Web API
   * SwaggerUI & ReDoc API documentation
   * User registration with email verification & social(GitHub) login using `django-allauth <https://pypi.org/project/django-allauth/>`_
   * `Bootstrap4 <https://pypi.org/project/django-bootstrap4/>`_ & `crispy-forms <https://pypi.org/project/django-crispy-forms/>`_ decorations
   * Customizable user profile pages with bio, profile pic, & `country flags <https://pypi.python.org/pypi/django-countries>`_
   * For links to additional package resources used in this repository, see the :doc:`Package Index <package_index>`
 * Dev/testing

   * Basic module testing templates
   * `Coverage <https://kevinbowen777.github.io/>`_ reports on web
   * `Debug-toolbar <https://pypi.org/project/django-debug-toolbar/>`_ available. See notes in `config/settings.py` for enabling.
   * Examples of using `Factories <https://pypi.org/project/factory-boy/>`_ & `pytest <https://pypi.org/project/pytest/>`_ fixtures in account app testing
   * `shell_plus <https://django-extensions.readthedocs.io/en/latest/shell_plus.html>`_ with `IPython <https://pypi.org/project/ipython/>`_ via `django-extensions <https://pypi.python.org/pypi/django-extensions/>`_ package
   * `Nox <https://pypi.org/project/nox/>`_ testing sessions for latest Python 3.9, 3.10, 3.11, 3.12, 3.13

     * `Sphinx <https://pypi.org/project/Sphinx/>`_ documentaion generation
     * linting

       * `ruff: <https://beta.ruff.rs/docs/>`_
     * `safety <https://pypi.org/project/safety/)(python package vulnerability testing>`_
     * `pytest sessions <https://docs.pytest.org/en/latest/>`_ with `pytest-cov <https://pypi.org/project/pytest-cov/>`_ & `pytest-django <https://pypi.org/project/pytest-django/>`_

Installation
------------

To install the django_api-library project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/django_api-library.git
   $ cd django_api-library

Local installation
------------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker installation
-------------------

.. code-block:: console

   $ docker compose up --build
   $ docker compose python manage.py migrate
   $ docker compose python manage.py createsuperuser
   Additional commands:
   $ docker compose exec web python manage.py shell_plus
     (loads Django shell autoloading project models & classes)
   $ docker run -it django-start-web bash`
     (CLI access to container)

Pre-commit installation
-----------------------
   To add the hook, run the following command in the poetry shell:
   $ pre-commit install

Usage
-----

To run django_api-library, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/resources/>`_

API URLs
----------------
 * Log In endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/login/>`_
 * Log Out endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/>`_
 * Password reset:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset>`_
 * Password reset confirmation:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm>`_
 * User registration endpoint:
    `<http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/>`_
 * User list:
    `<http://127.0.0.1:8000/api/v1/users/>`_
 * User detail:
    `<http://127.0.0.1:8000/api/v1/users/1/>`_
 * API schema download:
    `<http://127.0.0.1:8000/api/schema/>`_
 * Redoc API browser:
    `<http://127.0.0.1:8000/api/schema/redoc/>`_
 * Swagger-UI:
    `<http://127.0.0.1:8000/api/schema/swagger-ui/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -s coverage-3.13
   $ nox -s docs-3.11
   $ nox -rs lint-3.10  (Use the 'r' flag to reuse existing session)
   $ nox -s safety  (will run tests against all Python versions)
   $ nox -s tests

Application Demo
----------------
Live demonstration of application:

TBD

Reporting Bugs
--------------

Visit the django_api-library `Issues page <https://github.com/kevinbowen777/django-api-library/issues>`_ on GitHub.
