import pytest

from fuel import convert, gauge

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert('4/3')

def test_convert_negative_error():
    with pytest.raises(ValueError):
        convert('-4/3')
    with pytest.raises(ValueError):
        convert('4/-3')

def test_convert_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_convert_correct():
    assert convert('1/2') == 50
    assert convert('1/4') == 25
    assert convert('3/4') == 75

def test_gauge_full():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'

def test_gauge_empty():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'

def test_gauge_correct():
    assert gauge(50) == '50%'
    assert gauge(25) == '25%'
    assert gauge(75) == '75%'
