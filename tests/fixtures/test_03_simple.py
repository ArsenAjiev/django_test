import pytest


@pytest.fixture
def data_1():
    return 1


@pytest.fixture
def print_hello():
    print('\nHello')

#  использует фикстуры из этого файла
def test_data_1(data_1, print_hello):
    assert data_1 == 1

# использует фикстуру из tests/fixtures/conftest.py
def test_data_2(data_2):
    assert data_2 == 2

#  использует фикстуру из tests/conftest.py  на уровень выше
def test_data_3(data_3):
    assert data_3 == 3
