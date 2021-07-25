# # class Rectangle:
# #     def __init__(self, b):
# #         self.a =5
# #         self.b = b


# #     def perimeter(self):
# #         return 2 * (self.a + self.b)

# # rec1 = Rectangle(2)
# # print(rec1.perimeter())



# class Pryamougolnik:
#     def __init__(self, s1, s2):
#         self.a = s1
#         self.b = s2


#     def perimeter(self):
#         return 2 * (self.a + self.b)


#     def area(self):
#         return self.a * self.b
    

# rec1 = Pryamougolnik(5,4)
# print(rec1.perimeter())
# print(rec1.area())

# rec2 = Pryamougolnik(5,2)
# print(rec2.perimeter())
# print(rec2.area())


class Node:
    def __init__(self, val, l = None, r = None):
        self.val = val
        self.left = l
        self.right = r

# root = Node(2)
# root.left = Node(7)
# root.right = Node(5)

# print(root.val)
# print(root.left.val, root.right.val)

def insertToNode(values):
    if not root: return Node(values)
    elif root.val <= val:
        root.right = insertToNode(root.right, val)
    else:
        root.left = insertToNode(root.left, val)
    return root

values = [7,2,5]



    
