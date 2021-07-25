from random import randrange
import random


def get_numbers_ticket(min, max, quantity):
    if max <= min or quantity > max or min < 1 or max > 1000:
        return []
    a = [i for i in range(min,max)]

    return(sorted(random.sample(a, k=quantity)))





print(get_numbers_ticket(1,36, 2))