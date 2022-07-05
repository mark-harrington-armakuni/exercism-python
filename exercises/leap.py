def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif not (year % 100) == 0:
        if year % 4 == 0:
            return True

    return False
