from datetime import datetime, date, time, timedelta, timezone, tzinfo
import datetime

# a = datetime.date(2001, 8, 12)
# print(a)
# print(type(a))
# print(a.year)
# print(a.month)
# print(a.day)

# b = datetime.date.today()
# print(b)

# c = datetime.time(9, 12, 37, 557)
# print(c)
# print(type(c))

# d = datetime.time(13,28)
# print(d)

# e = datetime.time(23)
# print(e)


# print(c.hour)
# print(c.second)
# print(c.minute)
# print(c.second)
# print(c.microsecond)

# f = datetime.datetime(2007,11,23)
# print (f)
# g = datetime.datetime(2011,10,14,9,18,45,234)
# print(g)
# h = datetime.datetime.now()
# print(h)

# i = datetime.datetime.today()
# print(i)

# j = datetime.datetime.today().strftime("%d.%m.%Y")
# print(j)
# k = datetime.datetime.today().strftime("%H.%M.%S")
# print(k)
# l = datetime.datetime.now().strftime("%a.%A.%w.%b.%j")
# print(l)

# m = datetime.datetime(2015,3,27,8,12,24,654)
# print(m)
# print(m.year)
# print(m.month)
# print(m.day)
# print(m.hour)
# print(m.minute)
# print(m.second)
# print(m.microsecond)

# o = date(2015,3,19)
# print(o)
# p = time(5, 45, 38)
# print(p)
# q = datetime.datetime.combine(o,p)
# print(q)

# p = datetime.datetime.now()
# q = datetime.datetime(2015,3,21)
# r = p - q
# print(r)
# print(r.microseconds)
# print(r.days)
# print(r.seconds)

# s = timedelta (days=5, hours=21, minutes=2, seconds=37)
# print(s)

# print(type(s))

# t = datetime.datetime(2005,10,12)
# u = timedelta(days=45,hours=20)

# print(t+u)

# class UTC0600(tzinfo):
#     def __init__(self, offset = 21600, name = None):
#         self.offset = timedelta(seconds=offset)
#         self.name = name or self.__class__.__name__
#     def utcoffset(self, dt):
#         return self.offset
#     def tzname(self, dt):
#         return self.name
#     def dst(self, dt):
#         return timedelta(0)

# v = datetime.datetime.now(timezone.utc)
# print (v)     
# w = datetime.datetime.now(UTC0600())
# print(w)
# print(w.utcoffset())
# print(w.tzname())
# print(w.dst())



# xs = [215,9,58]
# print(sorted(xs))
# print(list(reversed(xs)))
# xs.sort()
# print(xs)

xr = ["vasya", "aristarh", "goga"]
print(sorted(xr, key=len, reverse=False))

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)

l1 = [( 1, 2, 3), (3, 1, 1), (8, 5, 3), (3, 4, 2)]

# Сортировка по второму элементу в кортеже.
# Lambda-функция возвращает второй элемент в кортеже.
print(sorted(l1, key=lambda x: x[1]))

from operator import itemgetter

l1 = [(1, 2, 3), (3, 1, 1), (8, 5, 3), (3, 4, 2)]

# Сортировка по третьему элементу в кортеже
print(sorted(l1, key=itemgetter(2)))

from typing import List


def fib(n:int) -> List(int):
    fib1: int = 1
    fib2: int = 1
    res = []
    for _ in range(n):
        res.append (fib1)
        fib1,fib2 = fib2,fib1+fib2
    return res
print(fib(8))