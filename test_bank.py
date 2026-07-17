import pytest

import pytest

try:
    from bank import value
except Exception:
    pass

def test_Value_start_with_Hello():
    assert value('Hello') == 0

def test_Value_start_with_hello():
    assert value('hello') == 0

def test_Value_start_with_H():
    assert value('Hi') == 20

def test_Value_start_with_h():
    assert value('hi') == 20

def test_Value_not_start_with_h():
    assert value('oh hello there') == 100
