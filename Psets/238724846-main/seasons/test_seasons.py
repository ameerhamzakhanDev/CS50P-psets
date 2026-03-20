import pytest
from datetime import datetime, timedelta
from seasons import DateToMin

def test_verify_date_valid():
    # Test valid date
    DateToMin.verify_date("2022-01-01")

def test_verify_date_invalid():
    # Test invalid date
    with pytest.raises(SystemExit):
        DateToMin.verify_date("01-01-2022")

def test_convert_date():
    # Test date conversion
    today = datetime.today()
    one_year_ago = today - timedelta(days=365)
    two_years_ago = today - timedelta(days=730)

    date_one_year_ago = one_year_ago.strftime("%Y-%m-%d")
    date_two_years_ago = two_years_ago.strftime("%Y-%m-%d")

    result_one_year_ago = DateToMin.convert(date_one_year_ago)
    result_two_years_ago = DateToMin.convert(date_two_years_ago)

    assert "minutes" in result_one_year_ago
    assert "minutes" in result_two_years_ago

def test_convert_leap_year():
    # Test leap year
    leap_year_date = "2020-01-01"
    result_leap_year = DateToMin.convert(leap_year_date)
    assert "minutes" in result_leap_year

def test_verify_date():
    # Test that passing an invalid format raises a SystemExit
    with pytest.raises(SystemExit):
        DateToMin.verify_date("January 1, 1999")

    with pytest.raises(SystemExit):
        DateToMin.verify_date("1999/12/31")
