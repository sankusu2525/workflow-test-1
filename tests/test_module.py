from src.module import foo

def test_foo():
    assert foo(2, 3) == 5
    assert foo(-1, 1) == 0
    assert foo(0, 0) == 0