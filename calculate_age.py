import datetime

birth_year = 1996
birth_month = 2
birth_day = 29

def calculate_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age

age = calculate_age(birth_year, birth_month, birth_day)
print(f"Your age is: {age}")