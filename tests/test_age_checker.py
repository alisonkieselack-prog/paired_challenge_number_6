from lib.age_checker import *
import pytest

"""
Given a date of birth that is above the age of 16
It returns a message saying that access is granted
"""
def test_age_above_16():
    assert age_checker("2002-06-23") == "Access has been granted."

"""
Given a date of birth that is under the age of 16
It returns a message saying that access is granted
"""
def test_age_under_16():
    assert age_checker("2020-06-23") == "Access has been denied. You are too young - your age is 6 and the required age is 16."

"""
Given a date of birth that is 16
It returns a message saying that access is granted
"""
def test_age_is_16():
    assert age_checker("2010-06-23") == "Access has been granted."

"""
Given a date of birth that is in the wrong format
It returns an Exception error and rejects it
"""
def test_date_not_in_correct_format():
    with pytest.raises(Exception) as e:
        age_checker("23-06-2020")
    error = str(e.value)
    assert error == "Please enter DOB in format 'YYYY-MM-DD'"

