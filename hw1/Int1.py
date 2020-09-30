import random
import pytest
import math


@pytest.fixture()
def random_value2():
    print('entering')
    yield random.randint(0, 20)
    print('exiting')


def test_int1():
    x = 3
    y = 4
    x = abs(x - y)
    assert x == 1


@pytest.mark.parametrize('x', (range(-5, 5)))
def test_int2(x):
    assert x == abs(x)


def test_int3():
    x = 3
    y = 4
    x = divmod(x, y)
    assert x == (0, 3)


def test_int4():
    x = complex(2, 3)
    y = complex(3, -8)
    z = x + y
    assert z == (5 - 5j)


def test_int5():
    a = math.pi
    a = round(a)
    assert a == 3
