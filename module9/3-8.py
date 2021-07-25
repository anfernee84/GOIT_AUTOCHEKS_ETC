
from datetime import datetime


def get_str_date(date):
    d = date.split(' ')[0]
    dt = datetime(year=int(d.split("-")[0]), month=int(d.split("-")[1]), day=int(d.split("-")[2]))
    dte = dt.strftime('%A %d %B %Y') 
    return(dte)





print(get_str_date("2021-05-27 17:08:34.149Z"))