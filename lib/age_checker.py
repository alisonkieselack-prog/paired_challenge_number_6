import datetime
from datetime import date

def age_checker(dobby):
    try:
        datetime.datetime.strptime(dobby, "%Y-%m-%d").date()
    except ValueError:
        raise Exception("Please enter DOB in format 'YYYY-MM-DD'")
    
    date_dobby = datetime.datetime.strptime(dobby, "%Y-%m-%d").date()
    day_diff = (date.today() - date_dobby).days
    age = day_diff//365

    if age >= 16:
        return "Access has been granted."
    
    return f"Access has been denied. You are too young - your age is {age} and the required age is 16."