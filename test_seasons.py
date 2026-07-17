import pytest
from datetime import date
from seasons import minutes_between

def test_minutes_calculation():
    assert minutes_between(date(1999, 1, 1), date(2000, 1, 1)) == 525600
    assert minutes_between(date(2001, 1, 1), date(2003, 1, 1)) == 1051200

def test_invalid_date():
    with pytest.raises((ValueError, SystemExit)):
        date.fromisoformat('February 6th, 1998')
    with pytest.raises((ValueError, SystemExit)):
        date.fromisoformat('01-01-1999')
