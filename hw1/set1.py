import pytest


@pytest.mark.parametrize('x', list(range(3)))
def test_set1(x):
    a = {'a', 'b', 'c', 'b'}
    a.add(x)
    assert a == {'a', 'b', 'c', 'b', x}


def test_set2():
    a = {'a', 'b', 'c', 'b'}
    a.remove('a')
    assert a == {'c', 'b'}


def test_set3():
    a = {'a', 'b', 'c', 'b'}
    a.clear()
    assert a == set()


def test_set4():
    a = {i ** 3 for i in range(5)}
    b = {27, 64, 8, 125}
    c = {8, 125}
    a = set.intersection(c, b, a)
    assert a == {8}


def test_set6():
    b = {512, 64}
    c = set.copy(b)
    assert c == {512, 64}
