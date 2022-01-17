import pytest

@pytest.fixture
def fixt(request):
    print('Begin in fixt')
    print(f'Call from {request.function.__name__}')
    yield
    print('Rolling back in fixt')


