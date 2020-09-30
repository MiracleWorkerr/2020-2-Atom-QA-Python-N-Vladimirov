import pytest


@pytest.mark.parametrize('x', list(range(3)))
def test_string1(x):
    a = ['a', 'b', 'c', 'b']
    a.append(x)
    assert a == ['a', 'b', 'c', 'b', x]


def test_string2():
    s1 = 'technoatom'
    s2 = 'qwerty'
    s = s1 + s2
    assert s == 'technoatomqwerty'


def test_string3():
    s = 'technoatom'
    s1 = 'qwerty'
    s = s[2:9:3]
    s = s + s1
    assert s == 'cooqwerty'


def test_string4():
    s = 'technoatom'
    s = str.isalpha(s)
    assert s == True


def test_string5():
    s = 'TechNoaTom'
    s = str.swapcase(s)
    assert s == 'tECHnOAtOM'
