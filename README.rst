A Django startproject template
==============================

Read up on Django startporject templates in the official documentation [1]_.


About
-----

This started out as a copy of the original Django template and a few things 
were added or modified:

- based on Django 1.9.1 template
- make settings a module (default uses `settings.dev`)
- add version.py
- add requirements (uses pip-tools)


Usage
-----

To create a new project called "foo" run startproject either directly from
the latest archive from github::

    django-admin startproject --template=https://github.com/fdemmer/django_project_template/archive/master.zip foo

Or from a local copy (with new django module/command example)::

    python -m django startproject --template=master.zip foo


.. [1] https://docs.djangoproject.com/en/1.9/ref/django-admin/#django-admin-startproject
