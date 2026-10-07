# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

```python
# EXAMPLE

def age_checker(text):
    """Checks whether a user is old enough to be admitted to a venue.

    Parameters: 
        date_of_birth: a string in the format "YYYY-MM-DD".
    
    Returns:
        a string letting the user know whether they are granted access or denied.

    Side effects:
        No side effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a date of birth that is above the age of 16
It returns a message saying that access is granted
"""
age_checker("2002-06-23") => "Access has been granted."

"""
Given a date of birth that is under the age of 16
It returns a message saying that access is granted
"""
age_checker("2020-06-23") => "Access has been denied. You are too young - your age is 6 and the required age is 16."

"""
Given a date of birth that is 16
It returns a message saying that access is granted
"""
age_checker("2010-06-23") => "Access has been granted."

"""
Given a date of birth that is in the wrong format
It returns an Exception error and rejects it
"""
age_checker("23-06-2020") => "Exception: Please enter DOB in format "YYYY-MM-DD""

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!