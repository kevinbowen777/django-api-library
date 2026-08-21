.. _`changelog`:

=========
Changelog
=========

``django-api-library`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-api-library/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-api-library 0.3.5 (2026-08-21)
=====================================

Improved documentation
----------------------

-  (`#599 <https://github.com/kevinbowen777/django-api-library/issues/599>`_): Add towncrier 25.8.0.


New features
------------

-  (`#624 <https://github.com/kevinbowen777/django-api-library/issues/624>`_): Upgrade to Django 6.0.8

django-api-library 0.3.4 (2026-07-31)
=====================================

Contributor-facing changes
--------------------------

-  (`#575 <https://github.com/kevinbowen777/django-api-library/issues/575>`_): Add Python 3.14 support.

-  (`#618 <https://github.com/kevinbowen777/django-api-library/issues/618>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#620 <https://github.com/kevinbowen777/django-api-library/issues/620>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#614 <https://github.com/kevinbowen777/django-api-library/issues/614>`_): Drop support for Python 3.11.


New features
------------

-  (`#583 <https://github.com/kevinbowen777/django-api-library/issues/583>`_): Upgrade Django to 6.0.7.

django-api-library 0.3.3 (2025-05-06)
=====================================

Contributor-facing changes
--------------------------

-  (`#518 <https://github.com/kevinbowen777/django-api-library/issues/518>`_): Upgrade PostgreSQL to 15.11.

-  (`#529 <https://github.com/kevinbowen777/django-api-library/issues/529>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#524 <https://github.com/kevinbowen777/django-api-library/issues/524>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#523 <https://github.com/kevinbowen777/django-api-library/issues/523>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#466 <https://github.com/kevinbowen777/django-api-library/issues/466>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#528 <https://github.com/kevinbowen777/django-api-library/issues/528>`_): Upgrade Django Rest Framework to 3.16.0.

-  (`#530 <https://github.com/kevinbowen777/django-api-library/issues/530>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#533 <https://github.com/kevinbowen777/django-api-library/issues/533>`_): Replace safety package with pip-audit.

django-api-library 0.3.2 (2025-01-22)
=====================================

Contributor-facing changes
--------------------------

-  (`#463 <https://github.com/kevinbowen777/django-api-library/issues/463>`_): Add support for Python 3.13

-  (`#506 <https://github.com/kevinbowen777/django-api-library/issues/506>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#497 <https://github.com/kevinbowen777/django-api-library/issues/497>`_): Upgrade Django to 5.1.4

django-api-library 0.3.0 (2023-12-23)
=====================================

Contributor-facing changes
--------------------------

- : Migrate to non-root Docker user & venv.

-  (`#212 <https://github.com/kevinbowen777/django-api-library/issues/212>`_): Update Python to 3.12.0.

-  (`#365 <https://github.com/kevinbowen777/django-api-library/issues/365>`_): Upgrade Poetry to 1.7.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#362 <https://github.com/kevinbowen777/django-api-library/issues/362>`_): Drop support for Python 3.9.


Improved documentation
----------------------

- : Update Sphinx theme to Furo


New features
------------

-  (`#373 <https://github.com/kevinbowen777/django-api-library/issues/373>`_): Upgrade to Django 5.0.

django-api-library 0.2.0 (2023-05-15)
=====================================

Contributor-facing changes
--------------------------

-  (`#244 <https://github.com/kevinbowen777/django-api-library/issues/244>`_): Install ruff. Drop flake8-* packages.

django-api-library 0.1.0 (2023-05-08)
=====================================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Migrate from pipenv to Poetry

- : Mirror to GitLab.

-  (`#11 <https://github.com/kevinbowen777/django-api-library/issues/11>`_): Add django-debug-toolbar.

-  (`#205 <https://github.com/kevinbowen777/django-api-library/issues/205>`_): Migrate from SQLite to PostgreSQL

-  (`#217 <https://github.com/kevinbowen777/django-api-library/issues/217>`_): Add support for Python 3.12.

-  (`#224 <https://github.com/kevinbowen777/django-api-library/issues/224>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#228 <https://github.com/kevinbowen777/django-api-library/issues/228>`_): Upgrade PostgreSQL to 15.2

-  (`#425 <https://github.com/kevinbowen777/django-api-library/issues/425>`_): Upgrade Django to 4.2.1


Improved documentation
----------------------

- : Add Sphinx for documentation

django-api-library 0.0.1 (2022-05-23)
=====================================

Contributor-facing changes
--------------------------

- : Add support for Python 3.10


New features
------------

- : Support Django 4.0.4


Miscellaneous internal changes
------------------------------

- : Initial commit
