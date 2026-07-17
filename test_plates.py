import pytest

from plates import is_valid

def test_is_valid_under_2_letters():
    assert is_valid('s') == False

def test_is_valid_over_6_letters():
    assert is_valid('allowed') == False

def test_is_valid_between_2_to_6_letters():
    assert is_valid('hello') == True

def test_is_valid_first_char_must_be_letter():
    assert is_valid('1A') == False

def test_is_valid_second_char_must_be_letter():
    assert is_valid('A1') == False

def test_is_valid_numbers_in_middle():
    assert is_valid('cs50p') == False

def test_is_valid_numbers_start_0():
    assert is_valid('cs05') == False

def test_is_valid_numbers_not_start_0():
    assert is_valid('cs50') == True

def test_is_valid_punctuation():
    assert is_valid('cs50!') == False
    assert is_valid('cs 50!') == False

