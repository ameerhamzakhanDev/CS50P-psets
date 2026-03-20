from working import convert
import pytest

def test_correct_time():
    assert convert("9 PM to 5:30 PM") == "21:00 to 17:30"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_value_error():
    # Test minutes > 59
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

    # Test invalid hour (like 13 AM)
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")

    # Test invalid format (missing "to")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    # Test garbage input
    with pytest.raises(ValueError):
        convert("cat")
