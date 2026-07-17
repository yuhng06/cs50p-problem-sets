import pytest
from project import validate_ticker, calculate_gain_loss, calculate_current_value

def test_validate_ticker():
    assert validate_ticker('D05.SI') == True
    assert validate_ticker('O39.SI') == True
    assert validate_ticker('D05') == False
    assert validate_ticker('039.SI') == True
    assert validate_ticker('cat') == False

def test_calculate_gain_loss():
    assert calculate_gain_loss(10.0, 12.0, 100) == 200.0
    assert calculate_gain_loss(10.0, 8.0, 100) == -200.0
    assert calculate_gain_loss(10.0, 10.0, 100) == 0.0

def test_calculate_current_value():
    assert calculate_current_value(12.0, 100) == 1200.0
    assert calculate_current_value(0.5, 200) == 100.0
    assert calculate_current_value(66.76, 100) == pytest.approx(6676.0)
