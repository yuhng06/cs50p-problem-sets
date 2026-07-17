from um import count

def test_valid_word():
    assert count('Um') == 1
    assert count('Um, um') == 2
    assert count('Umbrella') == 0

def test_space():
    assert count('where um where um') == 2

def test_capitalisation():
    assert count('UM UM') == 2
    assert count('UMMMM') == 0

def test_puntuation():
    assert count('UM!') == 1
    assert count('um?') == 1
    assert count('um,') == 1
