from collections import deque

MAX_LEN = 3

lifo = deque(maxlen=MAX_LEN)


def push(element):
    return lifo.appendleft(element)
    


def pop():
    return lifo.popleft()


















# d = deque()
# d.append('last')
# d.appendleft('first')
# d.insert(1, 'middle')
# print(d)      