import pytest


def test_list1():
    a = ['sss', 777, 4, 777, 'php', 0, '342']
    a.remove(777)
    assert a == ['sss', 4, 777, 'php', 0, '342']


@pytest.mark.parametrize('x', list(range(3)))
def test_list2(x):
    a = [99]
    a.insert(1, x)
    assert a == [99, x]


def test_list3():
    b = ['z', 45, 45, 'cc', 45, 'cc']
    b.insert(3, 'o')
    assert b == ['z', 45, 45, 'o', 'cc', 45, 'cc']


def test_list4():
    a = ['sss', 777, 4, 777, 'php', 0, '342']
    a.reverse()
    assert a == ['342', 0, 'php', 777, 4, 777, 'sss']


def test_list5():
    a = ['sss', 777, 4, 777, 'php', 0, '342']
    a.clear()
    assert a == []
