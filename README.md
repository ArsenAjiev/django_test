Pytest is a framework that makes building simple and scalable tests easy.
====

# install
      pip install pytest-django


# pytest.ini
      [pytest]
      DJANGO_SETTINGS_MODULE = django_test.settings
      python_files = tests.py test_*.py *_tests.py


# execute
      pytest
      pytest -s -v 
      pytest -s -v  tests/
      pytest -s -v  tests/test_sample.py



