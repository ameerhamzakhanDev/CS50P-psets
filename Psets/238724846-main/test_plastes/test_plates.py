import pytest
from plates import is_valid

def test_true():
    assert is_valid("AS202") == True

def test_false():
    assert is_valid("202") == False
    assert is_valid("AS02") == False
    assert is_valid("AS2222222") == False
    assert is_valid("AS2a") == False
    assert is_valid("AS2!?") == False
