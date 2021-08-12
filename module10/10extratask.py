# class Human:
#     counter = 0


#     def __init__(self, name):
#         self.name = name
#         Human.counter += 1

#     def how_many_persons(self):
#         return  f"the total amount of person is {Human.counter}"


# if __name__ == "__main__":
#     first = Human("Adam")
#     print (first.counter)
#     print (first.how_many_persons())

#     second = Human("Eve")
#     print (second.counter)    
#     print (second.how_many_persons())





# def flatten(items):
#     if len(items) == 0:
#         return []
#     item = items[0]

#     if not isinstance (item, list):
#         return [item] + flatten(items [1:])
#     return flatten (item) + flatten(items [1:])
        

# if __name__ == "__main__":
#     items = [1,2,3,[4,5],6,7,[8,9,10,11,12],[[[6,3,2,1],6,8,9,0,4,3]]]
#     print(flatten(items))

# def main ():
#     data = {
#         "first_name": "Sam",
#         "second_name": "Brown",
#         "age":45
#     }

#     with open("data.txt","w") as f:
#         f.write (
#             ",".join ([
#                 data["first_name"],
#                 data["second_name"],
#                 str(data["age"])
#                 ])
#             )

# if __name__ == "__main__":
#     main()


from hero import *

myhero1 = Hero("Vasya", 12, "urkagun")
myhero2 = SuperHero("Onufriy", 14, "buhar", 5)

myhero1.show_hero()
myhero2.show_hero()
myhero2.makemagic()
myhero2.show_hero()
