from datetime import datetime

def get_days_from_today(date):
    current_datetime = datetime.now()
    now = datetime(year=current_datetime.year, month=current_datetime.month, day=current_datetime.day)
    then = datetime(year=int(date.split("-")[0]), month=int(date.split("-")[1]), day=int(date.split("-")[2]))
    diff = now - then
    return(diff.days)





print(get_days_from_today("2021-10-09"))