### Packages
django==5.0.4
python-dotenv==1.0.1
djangorestframework==3.15.1
pytest==8.1.2
pytest-django==4.8.0


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
```python
pip install pytest
pip install pytest-django

### Example using pytest.ini

# -- FILE: pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = test.settings
# -- recommended but optional:
python_files = tests.py test_*.py *_tests.py

### Test
pytest -h   # get help
pytest      # perform test

