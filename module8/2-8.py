from calendar import monthrange


def get_days_in_month(month, year):
    return(monthrange(year, month)[1])



print(get_days_in_month(11, 1994))