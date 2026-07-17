import pytest

from twttr import shorten

def test_shorten_lowercase_vowels():
    assert shorten('hello') == 'hll'

def test_shorten_uppercase_vowels():
    assert shorten('HELLO') == 'HLL'

def test_shorten_mixed_case():
    assert shorten('Hello') == 'Hll'

def test_shorten_numbers():
    assert shorten('cs50') == 'cs50'

def test_shorten_punctuation():
    assert shorten('hello!') == 'hll!'
