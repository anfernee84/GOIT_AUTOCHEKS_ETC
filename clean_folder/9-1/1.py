from random import randint

def interval_generator():
    answer = []
    while len(answer)<10:
        print(answer)
        i = randint (1,10)
        if i not in answer:
            yield i
            answer.append(i)

gen = interval_generator()
k = 0
print("----------")
next(gen)
print("----------")
next(gen)
print("----------")
next(gen)
for i in gen:
        print(k)
        k += 1
