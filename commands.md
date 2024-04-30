### Packages
django==5.0.4
python-dotenv==1.0.1
djangorestframework==3.15.1
pytest==8.1.2
pytest-django==4.8.0
black=24.4.2
django-mptt=0.16.0
drf-spectacular=0.27.2
coverage=7.5.0
pytest-cov=5.0.0

### start a project
django-admin startproject drfecommerce .

./manage.py runserver

### get inside shell and execute commands 
```python
python manage.py shell 

# generate a secret key
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

### generate the current installed dependendencies
```python
pip freeze > requirements.txt

# re-install all dependencies
pip install -r requirements.txt
```

### setup environment variables
https://pypi.org/project/python-dotenv/

```python
pip install python-dotenv
```
#### in settings.py
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

SECRET_KEY = os.environ.get("SECRET_KEY")


### intall pytest
### https://pypi.org/project/pytest/
### https://pytest-django.readthedocs.io/en/latest/
```
pip install pytest
pip install pytest-django
```
### Example using pytest.ini

#### -- FILE: pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = test.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py

#### Test
pytest -h   # get help
pytest      # perform test

### Setup API Documentation with DRF_SPECTACULAR
#### https://pypi.org/project/drf-spectacular/

```
pip install drf-spectacular

#### in settings.py

INSTALLED_APPS = [
    . . .
    "drf_spectacular",
    . . .
}

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS":"drf_spectacular.openapi.AutoSchema",
}


SPECTACULAR_SETTINGS = {
    "TITLE": "django DRF ECommerce",
    
}

// # in the commandline 
./manage.py spectacular --file schema.yml

```

### install testing tool called coverage
#### [coverage](https://coverage.readthedocs.io/en/7.5.0/)
pip install coverage

coverage run -m pytest   # this will create a .coverage file
coverage html            # this will create an html report

#### slternative commanline coverage
pip install pytest-cov

pytest --cov