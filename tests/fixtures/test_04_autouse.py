import pytest


@pytest.fixture(autouse=True)
def auto():
    print('\nAutouse fixture')


def test_01():
    print('test_01 started')


def test_02():
    print('test_02 started')


# collected 2 items
#
# tests/fixtures/test_04_autouse.py::test_01
# Autouse fixture
# test_01 started
# PASSED
# tests/fixtures/test_04_autouse.py::test_02
# Autouse fixture
# test_02 started
# PASSED
#
# =========================================================================================== 2 passed in 0.03s ============================================================================================