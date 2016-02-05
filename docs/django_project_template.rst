Django startproject template
============================

Read up on Django startproject templates in the official documentation [1]_.

The latest version of the template can be found on github [2]_.


About
-----

Basis for this template was the Django 1.9 standard template.
A few things were added or modified.

- based on Django 1.9.1 template
- make settings a module (default uses `settings.dev`)
- add version.py (`__version__` available via settings)
- add requirements
  - uses pip-tools
  - requirements organized by environment
  - `requirements.txt` points to `requirements/dev.txt`
- add extra packages
  - django-extensions


Usage
-----

This assumes, you already have a virtualenv with Django created and activated.

To create a new project called "foo" run startproject either directly from
the latest archive from github::

    django-admin startproject --template=https://github.com/fdemmer/django_project_template/archive/master.zip foo

Or from a local copy (with new django module/command example)::

    python -m django startproject --template=master.zip foo

After that change into your new project directory "foo" and update 
the virtualenv with the recommended dev requirements::

    cd foo
    pip install -r requirements.txt

Enjoy your new Django project::

    ./manage.py shell_plus


.. [1] https://docs.djangoproject.com/en/1.9/ref/django-admin/#django-admin-startproject
.. [2] https://github.com/fdemmer/django_project_template

