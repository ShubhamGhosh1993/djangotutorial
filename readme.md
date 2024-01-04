Create a virtual environment:
python -m venv <environment_name>

Activate the environment:
Linux: source venv/bin/activate
Windows: venv/bin/activate


Master command for django project setup and details:
django-admin

Create  a project with django framework:
django-admin startproject <projectname>

Run the dev server by the following syntax:
python3 manage.py runserver <portnumber (optional)>

Default migrations
python3 manage.py migrate

Create a superuser to login in admin dashboard:
python3 manage.py createsuperuser
