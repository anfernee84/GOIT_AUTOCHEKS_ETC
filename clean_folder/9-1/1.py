# from random import randint

# def interval_generator():
#     answer = []
#     while len(answer)<10:
#         print(answer)
#         i = randint (1,10)
#         if i not in answer:
#             yield i
#             answer.append(i)

# gen = interval_generator()
# k = 0
# print("----------")
# next(gen)
# print("----------")
# next(gen)
# print("----------")
# next(gen)
# for i in gen:
#         print(k)
#         k += 1

# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
 
# def makeitalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
 
# @makebold
# @makeitalic
# def hello():
#     return "hello habr"
 
# print (hello())


def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)

print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))