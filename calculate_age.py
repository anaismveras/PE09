import datetime

def calculate_age(year, month, day):
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age