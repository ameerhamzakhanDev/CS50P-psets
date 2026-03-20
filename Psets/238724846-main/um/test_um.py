import pytest
from um import count


def test_single_match():
    assert count("I have an um") == 1


def test_multiple_matches():
    assert count("I have um and another um") == 2


def test_no_matches():
    assert count("There is noum in this sentence") == 0


def test_um_at_end_of_sentence():
    assert count("I have an um.") == 1


def test_um_with_punctuation():
    assert count("I have an Um, and another one is um?") == 2


def test_case_insensitive():
    assert count("I have a UM and another uM") == 2
