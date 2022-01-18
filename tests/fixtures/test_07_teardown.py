import pytest

# первый способ , более понятный
@pytest.fixture
def fixt(request):
    print('\nBegin in fixt')
    print(f'Call from {request.function.__name__}')
    yield
    print('\nRolling back in fixt')

#  второй способ больше кода , сложнее для понимания
@pytest.fixture
def fixt_fin(request):
    print('\nBegin in fixt_fin')
    print(f'Call from {request.function.__name__}')

    def fin():
        print('\nRolling back in fix_fin')

    request.addfinalizer(fin)


def test_01(fixt):
    print('test_01 started')


def test_02(fixt_fin):
    print('test_02 started')



# tests/fixtures/test_07_teardown.py::test_01 Begin in fixt
# Call from test_01
# test_01 started
# PASSED
# Rolling back in fixt
#
# tests/fixtures/test_07_teardown.py::test_02 Begin in fixt_fin
# Call from test_02
# test_02 started
# PASSED
# Rolling back in fix_fin
