import pytest

# нельзя использовать возвращаемое значение - return
@pytest.fixture
def class_fixt():
    print('\n class_fixt started')

# передали class_fixt через  usefixtures
@pytest.mark.usefixtures('class_fixt')
class TestSomething:
    def test_3(self):
        print('test_3 started')

    def test_4(self):
        print('test_4 started')


# tests/fixtures/test_05_usefixtures.py::TestSomething::test_3
#  class_fixt started
# test_3 started
# PASSED
# tests/fixtures/test_05_usefixtures.py::TestSomething::test_4
#  class_fixt started
# test_4 started
# PASSED

