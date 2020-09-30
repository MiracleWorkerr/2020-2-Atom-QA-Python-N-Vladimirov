import pytest


def test_dict1():
    d = {'dict1': 1, 'dict2': 2}
    d['dict3'] = 5 ** 2
    assert d == {'dict1': 1, 'dict2': 2, 'dict3': 25}


def test_dict2():
    d = dict(e='dict', r='diction')
    d.popitem()
    assert d == {'e': 'dict'}


@pytest.mark.parametrize('x', list(range(4)))
def test_dict3(x):
    d = {'dict1': 1, 'dict2': 2}
    d['dict3'] = x
    assert d == {'dict1': 1, 'dict2': 2, 'dict3': x}


def test_dict4():
    d = dict.fromkeys(['q', 'w'], 5)
    a = dict.copy(d)
    assert a == {'q': 5, 'w': 5}


def test_dict5():
    d = {a: a ** 3 for a in range(6)}
    v = {a: a ** 2 for a in range(8)}
    d.update(v)
    assert d == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
