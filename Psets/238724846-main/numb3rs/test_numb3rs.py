from numb3rs import validate

def test_correct_ip():
    assert validate("2.2.2.2") == True
    assert validate("225.225.225.225") == True
    assert validate("0.0.0.0") == True

def test_incorrect_ip():
    assert validate("-2.-2.-2.-2") == False
    assert validate("cat") == False
    assert validate("275.2.3.1") == False
    assert validate("001.2.3.1") == False
    assert validate("1.275.1.1") == False
    assert validate("1.1.275.1") == False
    assert validate("1.1.1.275") == False
