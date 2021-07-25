from datetime import datetime
from collections import defaultdict

days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

user_list = [
    {'Mike': datetime(year=1997, month=10, day=3)},
    {'Olesya': datetime(year=1978, month=8, day=24)},
    {'Nikita': datetime(year=2000, month=5, day=10)},
    {'Orest': datetime(year=2002, month=8, day=11)},
    {'Danylo': datetime(year=2002, month=8, day=1)},
    {'Natalya': datetime(year=1976, month=9, day=3)},
    {'Roman': datetime(year=1978, month=10, day=16)},
    {'Bohdan': datetime(year=2007, month=7, day=23)},
    {'Rostyslav': datetime(year=2007, month=7, day=21)},
    {'Yulia': datetime(year=2002, month=7, day=22)},
    {'Arsen': datetime(year=2002, month=7, day=18)},
    {'Mykola': datetime(year=2002, month=7, day=17)},
    {'Yaroslav': datetime(year=2002, month=7, day=16)},
    {'Vlad': datetime(year=2002, month=7, day=17)},
    {'Ed': datetime(year=2002, month=7, day=16)},
]


def congratulate(users: list):
    birthday_current_week = defaultdict(list)
    birthday_next_week = defaultdict(list)
    start_of_year = datetime(year=datetime.now().year, month=1, day=1)
    while start_of_year.weekday() != 0:
        start_of_year = start_of_year.replace(day=start_of_year.day + 1)


    for employee in users:
        for ind, val in employee.items():
            val = val.replace(year=datetime.now().year)

            birthday_number_of_week = (val - start_of_year).days // 7

            current_number_of_week = (datetime.now() - start_of_year).days // 7

            if current_number_of_week == birthday_number_of_week:
                if val.weekday() <= 4:
                    birthday_current_week[val.weekday()].append(ind)
                else:
                    birthday_next_week[0].append(ind)

            if birthday_number_of_week == current_number_of_week + 1:
                birthday_next_week[val.weekday()].append(ind)


    print('This week we will congratulate!:\n')

    for el in sorted(birthday_current_week.items(), key=lambda t: t[0]):
        names_to_congratulate = ', '.join(el[1])
        print(f'{days_of_week[el[0]]}: {names_to_congratulate}')

    print('\nNext week we will congratulate!:\n')

    for el in sorted(birthday_next_week.items(), key=lambda t: t[0]):
        names_to_congratulate = ', '.join(el[1])
        print(f'{days_of_week[el[0]]}: {names_to_congratulate}')


congratulate(user_list)