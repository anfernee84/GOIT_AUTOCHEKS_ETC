from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):


    getcontext().prec = signs_count
    sum = 0
    for i in number_list:
        sum += Decimal(i)
    return(sum/len(number_list))






print(decimal_average([3, 5, 77, 23, 0.57], 6))