from numb3rs import validate

def test_valid_ip():
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True
    assert validate('140.247.235.144') == True

def test_out_of_range():
    assert validate('256.255.255.255') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False

def test_leading_zeros():
    assert validate('192.168.001.1') == False
    assert validate('000.001.010.100') == False

def test_wrong_format():
    assert validate('cat') == False
    assert validate('8.8.8') == False
    assert validate('10.10.10.10.10') == False
