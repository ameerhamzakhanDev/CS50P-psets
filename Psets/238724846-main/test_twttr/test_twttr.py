import pytest
from twttr import shorten

def test_string_shorten():
    assert shorten("Hello I'm Haze") == "Hll 'm Hz"

def test_int_shorten():
    assert shorten("I'm gonna call 911!") == "'m gnn cll 911!"
