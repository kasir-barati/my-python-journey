# [Django](https://www.djangoproject.com/)

-   ` pip3 install Django`
-   Create new django project: `django-admin startproject project_name`
    -   Wrong usage: `django-admin startproject eighth_dharma/drill_project`
-   .gitignore emerges from [this](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) and [this](https://github.com/jpadilla/django-project-template/blob/master/.gitignore).
-   Files
    -   `__init__.py` Basically let us to load any file int this directory into others packages as a package.
    -   `settings.py` Specific configuration for our **project**. We have two concept in Django, app which is the equivalent for modules in NestJS.
    -   `urls` contains our endpoints
    -   `wsgi.py` allow us to run apache for example and run our project on it
    -   `manage.py` is the equivalent of `package.json` scripts
